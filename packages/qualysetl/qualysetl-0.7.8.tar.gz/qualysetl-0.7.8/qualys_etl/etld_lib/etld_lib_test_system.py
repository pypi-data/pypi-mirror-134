#!/usr/bin/env python3
import time
import json
from pathlib import Path
import re
import gzip
from qualys_etl.etld_lib import etld_lib_config
from qualys_etl.etld_lib import etld_lib_credentials
from qualys_etl.etld_lib import etld_lib_functions
from qualys_etl.etld_lib import etld_lib_extract_transform_load
from qualys_etl.etld_lib import etld_lib_datetime
from qualys_etl.etld_knowledgebase import knowledgebase_02_workflow_manager
from qualys_etl.etld_host_list import host_list_02_workflow_manager
from qualys_etl.etld_host_list_detection import host_list_detection_02_workflow_manager
from qualys_etl.etld_asset_inventory import asset_inventory_02_workflow_manager


def validate_json_file(open_file_method=open, file_path: Path = Path()):
    last_characters = []
    validation_type = 'tail file'
    with open_file_method(file_path, "rt", encoding='utf-8') as read_file:
        last_characters_test_passed = False
        try:
            # light validation detecting closure of json with curly brace closure
            last_characters = tail_file_by_last_characters(open_file_method=open_file_method,
                                                           file_path=file_path,
                                                           number_of_characters=25)
            validate_last_characters_are_str = '}'
            if last_characters[-1:] == validate_last_characters_are_str:
                last_characters_test_passed = True
        except Exception as e:
            last_characters_test_passed = False

        try:
            if last_characters_test_passed is False:
                validation_type = 'json.load file'
                json.load(read_file)
        except Exception as e:
            raise Exception(f"WARNING: MALFORMED JSON, COULD NOT json.load batch file, "
                            f"validation_test_type={validation_type}, "
                            f"directory={Path(file_path).parent.name}, "
                            f"batch file={etld_lib_extract_transform_load.get_batch_name_from_filename(file_path)}, "
                            f"Exception={e}"
                            )

        etld_lib_functions.logger.info(f"PASS: JSON VALIDATED, "
                                       f"validation_test_type={validation_type}, "
                                       f"directory={Path(file_path).parent.name}, "
                                       f"batch file={etld_lib_extract_transform_load.get_batch_name_from_filename(file_path)}, "
                                       f"tail file={last_characters}")


def validate_extract_directories_json_files_downloaded():
    json_dir_list = []
    json_dir_list.append(Path(etld_lib_config.host_list_extract_dir))
    json_dir_list.append(Path(etld_lib_config.host_list_detection_extract_dir))
    json_dir_list.append(Path(etld_lib_config.kb_extract_dir))
    json_dir_list.append(Path(etld_lib_config.asset_inventory_extract_dir))
    json_dir_search_glob = '*.json.gz'

    for json_dir in json_dir_list:
        json_file_list = sorted(Path(json_dir).glob(json_dir_search_glob))
        for json_file_path in json_file_list:
            try:
                validate_json_file(open_file_method=gzip.open,
                                   file_path=json_file_path)
            except Exception as e:
                etld_lib_functions.logger.error(f'Exception {e}')


def tail_file_by_last_characters(open_file_method=open, file_path: Path = Path(), number_of_characters: int = 1000):
    file_position = number_of_characters
    last_lines_from_file = []
    file_length_in_utf_8_characters = 0
    with open_file_method(file_path, mode="rt", encoding='utf-8') as f:
        try:
            f.seek(0, 2)
            file_length_in_utf_8_characters = f.tell()
            if file_length_in_utf_8_characters <= number_of_characters:
                file_position = 0
            else:
                file_position = file_length_in_utf_8_characters - number_of_characters

            f.seek(file_position, 0)
            last_characters_list = []
            while True:
                char = f.read(1)
                if not char:
                    break
                last_characters_list.append(char)
        except IOError as ioe:
            raise Exception(ioe)
        finally:
            last_lines_from_file = ''.join(last_characters_list)
            return last_lines_from_file


def tail_file_by_lines(open_file_method=open, file_path: Path = Path(), number_of_lines: int = 10):
    file_position = number_of_lines + 1
    last_lines_from_file = []
    with open_file_method(file_path, mode="rt", encoding='utf-8') as f:
        while len(last_lines_from_file) <= number_of_lines:
            try:
                f.seek(-file_position, 2)
            except IOError:
                f.seek(0)
                break
            finally:
                last_lines_from_file = list(f)
            file_position *= 2
    return last_lines_from_file[-number_of_lines:]


def validate_xml_is_closed_properly(test_by='xml_characters',
                                    open_file_method=gzip.open,
                                    file_path: Path = Path(),
                                    number_of_lines: int = 10,
                                    number_of_characters: int = 1000):
    batch = re.sub('^.*batch', 'batch', str(file_path))
    directory_name = str(file_path.parent.name)
    xml_lines = []
    xml_characters_list = []
    try:
        if 'characters' in test_by:
            xml_lines = tail_file_by_last_characters(open_file_method, file_path, number_of_characters)
        else:
            xml_lines = tail_file_by_lines(open_file_method, file_path, number_of_lines)
    except Exception as e:
        xml_line = ''.join(xml_lines.replace('\n', ''))
        raise Exception(f"WARNING: CANNOT READ, CREATION MAY BE IN PROGRESS "
                        f"test_by={test_by} "
                        f"directory={directory_name} "
                        f"batch file={batch}, "
                        f"Exception={e}, "
                        f"tail file={xml_line}")

    found_end_of_response = False
    end_of_response = '</RESPONSE>'
    found_incident = False
    incident_text = 'incident signature'
    xml_line = ''.join(xml_lines.replace('\n', ''))
    if end_of_response in xml_line:
        found_end_of_response = True
    if incident_text in str(xml_line).lower():
        found_incident = True

    if found_incident is True:
        raise Exception(f"WARNING: INCIDENT FOUND, "
                        f"test_by={test_by} "
                        f"directory={directory_name} "
                        f"batch file={batch}, "
                        f"tail file={xml_line}")
    elif found_end_of_response is False:
        raise Exception(f"WARNING: END OF RESPONSE NOT FOUND, "
                        f"test_by={test_by} "
                        f"directory={directory_name} "
                        f"batch file={batch}, "
                        f"tail file={xml_line}")
    else:
        etld_lib_functions.logger.info(f"PASS: "
                                       f"test_by={test_by} "
                                       f"directory={directory_name} "
                                       f"batch file={batch}, "
                                       f"tail file={xml_line}")
    return xml_line


def validate_extract_directories_xml_files_downloaded(test_by='characters'):
    xml_dir_list = []
    xml_dir_list.append(Path(etld_lib_config.host_list_extract_dir))
    xml_dir_list.append(Path(etld_lib_config.host_list_detection_extract_dir))
    xml_dir_list.append(Path(etld_lib_config.kb_extract_dir))
    xml_dir_search_glob = '*.xml.gz'

    for xml_dir in xml_dir_list:
        xml_file_list = sorted(Path(xml_dir).glob(xml_dir_search_glob))
        for xml_file_path in xml_file_list:
            try:
                if 'characters' in test_by:
                    lines = validate_xml_is_closed_properly(open_file_method=gzip.open,
                                                            file_path=xml_file_path,
                                                            number_of_lines=8,
                                                            number_of_characters=1000)
                else:
                    lines = validate_xml_is_closed_properly(test_by='lines',
                                                            open_file_method=gzip.open,
                                                            file_path=xml_file_path,
                                                            number_of_lines=8,
                                                            number_of_characters=1000)
            except Exception as e:
                etld_lib_functions.logger.error(f'Exception {e}')


def test_knowledgebase(test_name='knowledgebase'):
    etld_lib_config.kb_last_modified_after = etld_lib_datetime.get_utc_date_minus_days(30)
    etld_lib_functions.logger.info(f"Starting test with kb_last_modified_after: {etld_lib_config.kb_last_modified_after}")
    try:
        knowledgebase_02_workflow_manager.main()
    except Exception as e:
        etld_lib_functions.logger.error(f"Failed Test: Exception{e}")
        raise Exception

    etld_lib_functions.logger.info(f"Ending   test with kb_last_modified_after: {etld_lib_config.kb_last_modified_after}")


def test_host_list(test_name='host_list'):
    etld_lib_config.host_list_vm_processed_after = etld_lib_datetime.get_utc_date_minus_days(180)
    etld_lib_config.host_list_test_system_flag = True
    etld_lib_config.host_list_test_number_of_files_to_extract = 3
    etld_lib_config.host_list_payload_option = {'truncation_limit': '25'}
    etld_lib_functions.logger.info(
        f"Starting test with: "
        f"host_list_vm_processed_after={etld_lib_config.host_list_vm_processed_after}, "
        f"host_list_payload_option={etld_lib_config.host_list_payload_option}, " 
        f"host_list_test_number_of_files_to_extract={etld_lib_config.host_list_test_number_of_files_to_extract}")
    try:
        host_list_02_workflow_manager.main()
    except Exception as e:
        etld_lib_functions.logger.error(f"Failed Test: Exception{e}")
        raise Exception

    etld_lib_functions.logger.info(f"Ending: {etld_lib_config.host_list_vm_processed_after}, "
                                   f"Test {etld_lib_config.host_list_test_number_of_files_to_extract} files")


def test_host_list_detection(test_name='host_list_detection'):
    etld_lib_config.host_list_detection_vm_processed_after = etld_lib_datetime.get_utc_date_minus_days(180)
    etld_lib_config.host_list_vm_processed_after = etld_lib_datetime.get_utc_date_minus_days(180)
    etld_lib_config.host_list_test_system_flag = True
    etld_lib_config.host_list_test_number_of_files_to_extract = 3
    etld_lib_config.host_list_payload_option = {'truncation_limit': '25'}
    etld_lib_functions.logger.info(
        f"Starting test with: "
        f"host_list_vm_processed_after={etld_lib_config.host_list_vm_processed_after}, "
        f"host_list_payload_option={etld_lib_config.host_list_payload_option}, " 
        f"host_list_test_number_of_files_to_extract={etld_lib_config.host_list_test_number_of_files_to_extract}")
    try:
        host_list_detection_02_workflow_manager.main()
    except Exception as e:
        etld_lib_functions.logger.error(f"Failed Test: Exception{e}")
        raise Exception

    etld_lib_functions.logger.info(f"Ending: {etld_lib_config.host_list_vm_processed_after}, "
                                   f"Test {etld_lib_config.host_list_test_number_of_files_to_extract} files")


def test_asset_inventory(test_name='asset_inventory'):
    etld_lib_config.asset_inventory_asset_last_updated = etld_lib_datetime.get_utc_date_minus_days(180)
    etld_lib_config.asset_inventory_test_system_flag = True
    etld_lib_config.asset_inventory_test_number_of_files_to_extract = 3
    etld_lib_functions.logger.info(
        f"Starting test with: "
        f"asset_inventory_asset_last_updated={etld_lib_config.asset_inventory_asset_last_updated}, "
        f"asset_inventory_test_number_of_files_to_extract="
        f"{etld_lib_config.asset_inventory_test_number_of_files_to_extract}")
    try:
        asset_inventory_02_workflow_manager.main()
    except Exception as e:
        etld_lib_functions.logger.error(f"Failed Test: Exception{e}")
        raise Exception

    etld_lib_functions.logger.info(
        f"Ending test with: "
        f"asset_inventory_asset_last_updated={etld_lib_config.asset_inventory_asset_last_updated}, "
        f"asset_inventory_test_number_of_files_to_extract="
        f"{etld_lib_config.asset_inventory_test_number_of_files_to_extract}")


def main():
    return_code = 0
    try:
        test_knowledgebase()
    except Exception as e:
        return_code = 1
    try:
        test_host_list()
    except Exception as e:
        return_code = 2
    try:
        test_host_list_detection()
    except Exception as e:
        return_code = 3
    try:
        test_asset_inventory()
    except Exception as e:
        return_code = 4
    try:
        validate_extract_directories_json_files_downloaded()
    except Exception as e:
        return_code = 5
    try:
        validate_extract_directories_xml_files_downloaded(test_by='characters')
    except Exception as e:
        return_code = 6
    exit(return_code)


if __name__ == "__main__":
    etld_lib_functions.main(my_logger_prog_name='etld_lib_test')
    etld_lib_config.main()
    etld_lib_credentials.main()
    main()
