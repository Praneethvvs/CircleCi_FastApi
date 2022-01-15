from fastapi import FastAPI, Path, Query, UploadFile, File
from pydantic import BaseModel
from selenium_pipeline.geo_data_automation import *
from selenium_pipeline.screenshot_with_sel import *
import pandas as pd
import aiofiles
import uvicorn
import random
from fastapi.middleware.cors import CORSMiddleware

class locationInfo(BaseModel):
    zip_code_list: list


app = FastAPI()

# origins = ["*"]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )



@app.post("/get_locations_for_zip/")
def location_module(value_list: locationInfo):
    results_list = []
    for zips in value_list.zip_code_list:
        try:
            results_list.append(get_results(zips))
        except:
            pass
    return {"status": "Success", "results": results_list}

@app.post("/get_locations_for_zip_from_excel/")
async def location_module(file:UploadFile= File(...)):
    outfile_path = "test.xlsx"
    async with aiofiles.open(outfile_path, 'wb') as out_file:
        content = await file.read()  # async read
        await out_file.write(content)  # async write

    data = pd.read_excel(r"C:\Users\Praneeth\PycharmProjects\PVVS-001\test.xlsx")
    results_list = []
    for index, zips in enumerate(data["Filtered_zip"].unique(),start=1):
        if index == 3:
            break
        try:
            results_list.append(get_results(zips))
        except:
            pass
    return {"status": "Success", "results": results_list}

@app.get("/screenshot/")
def screenshot_test():
    try:
        title = screenshot_main()
        return {"status": "success","title":title}
    except:
        return {"status":"error"}


@app.post("/random_function")
def random_number_gen(_range:int):
    return {"status":"success","random_list":random.sample(list(range(1,_range)),20)}

@app.post("/square_of_a_number")
def random_number_gen(number:int):
    return {"status":"success","result":number**2}

# if __name__ == "__main__":
#     uvicorn.run("application:app", host="0.0.0.0", port=7000,lifespan="on",reload=True)