#!/usr/bin/env python 3.8
# -*- coding: utf-8 -*-

'''
created on Sun Sep 5
'''

# Library imports
from typing import List, Optional
from fastapi.datastructures import UploadFile

from fastapi import FastAPI, Request, File, UploadFile, Depends
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import SQLModel, create_engine
from sqlmodel.orm.session import Session
from starlette.responses import Response
from data_models.models import bit_data

# import chart and stats
from utils.save_upload import save_uploaded_file
from utils.read_excel import parse_contents
from utils.get_session import create_session
from utils.draw_charts import draw_chart

# python modules
import time
import os, shutil
from pathlib import Path

# data processing
import pandas as pd

# Create app and model objects
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/upload", StaticFiles(directory="upload"), name="upload")
templates = Jinja2Templates(directory="templates/")
favicon_path = 'favicon.ico'


# set up sqllite db
data_engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/bit_data')

# load favicon
@app.get('/favicon.ico')
async def favicon():
    return FileResponse(favicon_path)


# Welcome page
@app.get("/", response_class=HTMLResponse)
#async def read_root(request:Request, db: Session = Depends(create_session)):
async def read_root(request:Request):
    # get a list of available features
    # bit_info = db.query(bit_data).first()
    # features = bit_info.__dict__.keys
    return templates.TemplateResponse("welcome.html",
    {"request": request})

# data properties page
@app.post("/uploadfile")
async def upload(request:Request,
                files: List[UploadFile] = File(...)):
    
    # upload files, kept multi file upload option for now
    for file in files:
        fn = file.filename
        folder_name = fn.split(".")[0]

        # create upload folder
        upload_folder = os.path.join('./upload', folder_name)
        try:
            os.makedirs(upload_folder)
        except OSError:
            shutil.rmtree(upload_folder)
            os.makedirs(upload_folder)

        p = Path(upload_folder +'/'+ fn)

        # exception handling for no files uploaded
        try:
            save_uploaded_file(file, p)
        except IsADirectoryError:
            message = 'no files uploaded, please try again'
            return templates.TemplateResponse("error_page.html", 
            {"request":request, 
            "message":message})

    # open file and get dataframe
    df_pred, _ = parse_contents(p, fn)
    df_pred.to_sql('bit_data', data_engine, if_exists='replace', index=False)
    features = df_pred.columns.tolist()

    return templates.TemplateResponse("list_data.html", 
    {"request": request, "features": features, "path": [p]})

# sql queries page
@app.get("/get-data")
async def get_data(request:Request):
    return templates.TemplateResponse("datatable.html", 
    {"request": request})

# sql queries page
@app.get("/display-data", response_class=HTMLResponse)
async def display_data(request:Request,
                       file_path: Optional[str] = None,
                       x_axis: Optional[str] = None,
                       y_axis: Optional[str] = None,
                       color: Optional[str] = None
                       ):
    
    # load dataframe
    print(file_path)
    print(x_axis)
    print(y_axis)
    print(color)
    df = pd.read_csv("upload/ToolRun small/ToolRun small.csv")
    features = df.columns.tolist()
    draw_chart(df, x_axis, y_axis, color)

    return templates.TemplateResponse("list_data.html", 
    {"request": request, "features": features,
    "path": ["upload/ToolRun small/ToolRun small.csv"]})
