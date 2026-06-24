from fastapi import APIRouter

from app.services.qa.candidate_compare import (
    compare_candidates
)

router = APIRouter()


@router.get("/compare")
async def compare(
    query: str
):

    return {

        "comparison":

        compare_candidates(
            query
        )

    }