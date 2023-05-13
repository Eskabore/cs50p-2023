def get_media_type(filename):
    lower_filename = filename.lower().strip()
    types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    for suffix, media_type in types.items():
        if lower_filename.endswith(suffix):
            return media_type
    return "application/octet-stream"

filename = input("File name: ")
media_type = get_media_type(filename)
print(f"{media_type}")
