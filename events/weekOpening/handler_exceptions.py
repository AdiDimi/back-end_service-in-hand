from fastapi import FastAPI, Request, status, HTTPException

class GetRequestTypeNotFoundException(HTTPException):
    def __init__(self, detail: str, status_code: int):
        self.status_code = status_code
        self.detail = detail

class InvalidActionException(HTTPException):
    def __init__(self, detail: str, status_code: int):
        self.status_code = status_code
        self.detail = detail
