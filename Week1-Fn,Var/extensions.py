print("File name: ", end = "")
resource = input()

if ".gif" in resource:
    print("image/gif")
elif ".jpg" in resource or ".jpeg" in resource:
    print("image/jpeg")
elif ".png" in resource:
    print("image/png")
elif ".pdf" in resource.lower():
    print("application/pdf")
elif ".txt" in resource:
    print("text/plain")
elif ".zip" in resource:
    print("application/zip")
else:
    print("application/octet-stream")
