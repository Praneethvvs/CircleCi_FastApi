import requests
from pprint import pprint
import xml.etree.ElementTree as ET
import pandas as pd



def get_address_info(address,city,state,zip):
    input_request = 'http://production.shippingapis.com/ShippingAPI.dll'

    params = {"API":"Verify","XML":f'''<AddressValidateRequest USERID="276PVVS06809"><Address ID="1"><Address1></Address1><Address2>{address}</Address2><City>{city}</City>
    <State>{state}</State><Zip5>{zip}</Zip5><Zip4></Zip4></Address></AddressValidateRequest>'''}

    res = requests.post(input_request,params=params)
    if res.status_code == 200:
        xml_content = ET.fromstring(res.content)
        try:
            result = xml_content.findall(".//Address2")[0].text
        except:
            result = xml_content.findall(".//Description")[0].text
    else:
        result = "request_failed"

    return result


def main(excel_name):
    address_df = pd.read_excel(excel_name)
    address_df.apply(lambda x:x.astype(str).str.strip())
    api_result = address_df.apply(lambda x:get_address_info(x.address,x.city,x.state,x.zip) ,axis = 1)
    address_df["results"] = api_result
    address_df.to_excel(f"{excel_name[:excel_name.rindex('.')]}_updated.xlsx",index=False)

if __name__ == "__main__":
    main("address_samples.xlsx")
