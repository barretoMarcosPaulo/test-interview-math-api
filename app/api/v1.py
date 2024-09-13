from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.domain.services import MathService
from app.domain.complex_number_library import Numbers
from pydantic import BaseModel

router = APIRouter()


class NumbersInput(BaseModel):
    numbers: List[int]


def get_math_service():
    return MathService(Numbers())


@router.post("/sum")
async def sum_numbers(
    input: NumbersInput, math_service: MathService = Depends(get_math_service)
):
    try:
        result = math_service.sum_numbers(input.numbers)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/average")
async def average_numbers(
    input: NumbersInput, math_service: MathService = Depends(get_math_service)
):
    try:
        result = math_service.average_numbers(input.numbers)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
