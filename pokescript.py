from pyscript import web, when

# This is how you change the text of an item
new_text = "Yes Boys"
header_access = web.page["main_header"]
header_access.innerText = new_text

print("Hello World")