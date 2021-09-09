#!/usr/bin/env python 3.8
# -*- coding: utf-8 -*-

'''
created on Sun Sep 5
'''

# Library imports
from typing import List, Optional
from fastapi.datastructures import UploadFile

from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import SQLModel, Field, create_engine
from starlette.responses import Response

# import chart and stats
from utils.save_upload import save_uploaded_file
from utils.read_excel import parse_contents

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

# setup for SQLmodels
class bit_data(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    bit_size: int = Field(default=0, nullable=False)
    bit_type: str = Field(default="", nullable=False)
    mfg: str = Field(default="")
    serial_no: str = Field(default="")
    depth_in: float = Field(default=0.0)
    depth_out: float = Field(default=0.0)
    distance: float = Field(default=0.0)
    hours: float = Field(default=0.0)
    rop: float = Field(default=0.0)
    inner: int = Field(default=0)
    outer: int = Field(default=0)
    main: str = Field(default="")
    loc: str = Field(default="")
    B: str = Field(default="X")
    G: float = Field(default=0.0)
    other: str = Field(default="")
    reason_pulled: str = Field(default="")
    well_name: str = Field(default="")
    opertor: str = Field(default="")
    lat: float = Field(default=0.0)
    lon: float = Field(default=0.0)

# set up sqllite db
engine = create_engine('sqlite:///bit_data.db')


# Welcome page
@app.get("/", response_class=HTMLResponse)
async def read_root(request:Request):
    # get a list of available features
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
    df_pred.to_sql(name='bit_data', con=engine, if_exists='append', index=False)

    return templates.TemplateResponse("datatable.html", 
    {"request": request, 
    "data_summary": [df_pred.to_html(table_id='table_id').replace('border="1"', ' ')]})

# sql queries page
@app.post("/get-data")
async def get_data(request:Request):
    return templates.TemplateResponse("datatable.html", 
    {"request": request})

# sql queries page
@app.post("/display-data")
async def display_data(request:Request, response = Response):
    
    # connect to db
    session = engine.connect()
    session.query("select * from bit_data")

    return templates.TemplateResponse("datatable.html", 
    {"request": request})
