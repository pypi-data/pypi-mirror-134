"""
converters module will convert data from one form to another form.
"""
import logging
import os
import pandas as pd
import pdfkit


def flatten(obj, keys):
    """
     It will flatten the dictionary object specified in the argument
     :param obj: object to be flattened
     :param keys: list of keys which are not flattened by default
     :return: reference of flattened object
    """
    for key in keys:
        values = obj[key]
        if values:
            for value in values:
                for k, val in value.items():
                    obj[k] = val
            del obj[key]
    return obj


class Converter:
    """
    converter class to convert a list of dictionary objects to various formats
    """
    @staticmethod
    def convert_to_csv(object_list, path):
        """
        converts list of dictionary objects to csv
         param object_list: list containing dictionary objects
         param path: output path of generated csv
        """
        if object_list is None:
            raise TypeError("object_list cannot be none")
        if not isinstance(object_list, list) or not isinstance(object_list[0], dict):
            raise TypeError("list of dictionaries is expected as input for object_list parameter")
        if path is None:
            raise TypeError("path cannot be none")
        try:
            dataframe = pd.DataFrame(data=object_list)
            dataframe.to_csv(path, index=False)
            # with open(path, 'w') as csvfile:
            #    writer = csv.DictWriter(csvfile, fieldnames=field_names)
            #    writer.writeheader()
            #    for obj in object_list:
            #        d = {key: value for key, value in obj.items() if key in field_names}
            #        writer.writerow(d)
        except PermissionError as p_e:
            logging.error("Permission error occurred in convert_to_csv func :%s", ({str(p_e)}))
        except FileNotFoundError as f_e:
            logging.error("FileNotFound error occurred in convert_to_csv func :%s", ({str(f_e)}))

    @staticmethod
    def convert_to_pdf(object_list, path):
        """
        converts list of dictionary objects to pdf
         : param object_list: list containing dictionary objects
         : param path: output path of generated pdf
        """
        if object_list is None:
            raise TypeError("object_list cannot be none")
        if not isinstance(object_list, list) or not isinstance(object_list[0], dict):
            raise TypeError("list of dictionaries is expected as input for object_list parameter")
        if path is None:
            raise TypeError("path cannot be none")
        try:
            dataframe = pd.DataFrame(data=object_list)
            temp_html_filename = "temp.html"
            dataframe.to_html(temp_html_filename)
            pdfkit.from_file(temp_html_filename, output_path=path,
                             options={"page-height": "2500", "page-width": "1270"})
            os.remove(temp_html_filename)
        except PermissionError as p_e:
            logging.error("Permission error occurred in convert_to_pdf func :%s", ({str(p_e)}))
        except FileNotFoundError as f_e:
            logging.error("FileNotFound error occurred in convert_to_pdf func :%s", ({str(f_e)}))

    @staticmethod
    def convert_to_html(object_list, path):
        """
        converts list of dictionary objects to html
          : param object_list: list containing dictionary objects
         : param path: output path of generated html
        """
        if object_list is None:
            raise TypeError("object_list cannot be none")
        if not isinstance(object_list, list) or not isinstance(object_list[0], dict):
            raise TypeError("list of dictionaries is expected as input for object_list parameter")
        if path is None:
            raise TypeError("path cannot be none")
        try:
            dataframe = pd.DataFrame(data=object_list)
            dataframe.to_html(path)
        except PermissionError as p_e:
            logging.error("Permission error occurred in convert_to_html func :%s", ({str(p_e)}))
        except FileNotFoundError as f_e:
            logging.error("FileNotFound error occurred in convert_to_html func :%s", ({str(f_e)}))

    @staticmethod
    def convert_to_xml(object_list, path):
        """
        converts list of dictionary objects to xml
          : param object_list: list containing dictionary objects
         : param path: output path of generated xml
        """
        if object_list is None:
            raise TypeError("object_list cannot be none")
        if not isinstance(object_list, list) or not isinstance(object_list[0], dict):
            raise TypeError("list of dictionaries is expected as input for object_list parameter")
        if path is None:
            raise TypeError("path cannot be none")
        try:
            dataframe = pd.DataFrame(data=object_list)
            dataframe.to_xml(path)
        except PermissionError as p_e:
            logging.error("Permission error occurred in convert_to_xml func :%s", ({str(p_e)}))
        except FileNotFoundError as f_e:
            logging.error("FileNotFound error occurred in convert_to_xml func :%s", ({str(f_e)}))

    @staticmethod
    def convert_to_excel(object_list, path):
        """
        converts list of dictionary objects to excel
          : param object_list: list containing dictionary objects
         : param path: output path of generated excel
        """
        if object_list is None:
            raise TypeError("object_list cannot be none")
        if not isinstance(object_list, list) or not isinstance(object_list[0], dict):
            raise TypeError("list of dictionaries is expected as input for object_list parameter")
        if path is None:
            raise TypeError("path cannot be none")
        try:
            dataframe = pd.DataFrame(data=object_list)
            dataframe.to_excel(path)
        except PermissionError as p_e:
            logging.error("Permission error occurred in convert_to_excel func :%s", ({str(p_e)}))
        except FileNotFoundError as f_e:
            logging.error("FileNotFound error occurred in convert_to_excel func :%s", ({str(f_e)}))
