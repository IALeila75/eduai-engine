import json
import uuid
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "output" / str(datetime.now().year)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def save_course(course, request):

    course_id = uuid.uuid4().hex[:8]

    filename = (
        f"{course_id}_"
        f"{request.matiere}_"
        f"{request.niveau}_"
        f"{request.theme}.json"
    )

    filename = filename.replace(" ", "_")

    filepath = OUTPUT_DIR / filename

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(
            course.model_dump(),
            f,
            ensure_ascii=False,
            indent=4
        )

    return filepath