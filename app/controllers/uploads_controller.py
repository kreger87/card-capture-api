from app.services.uploads_service import (
    upload_file_service,
    check_upload_status_service,
    get_image_service,
    bulk_upload_service,
    export_to_slate_service
)

async def upload_file_controller(background_tasks, file, event_id, school_id, user):
    return await upload_file_service(background_tasks, file, event_id, school_id, user)

async def check_upload_status_controller(document_id: str):
    return await check_upload_status_service(document_id)

async def get_image_controller(document_id: str):
    return await get_image_service(document_id)

async def bulk_upload_controller(background_tasks, file, event_id, school_id, user):
    return await bulk_upload_service(background_tasks, file, event_id, school_id, user)

async def export_to_slate_controller(payload: dict):
    return await export_to_slate_service(payload) 