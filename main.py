# Open the file in write mode
file = open("index.html", "w")

# Write HTML content
file.write("<html>")
file.write("<head>")
file.write("<title>My Webpage</title>")
file.write("</head>")
file.write("<body>")
file.write("<h1>Welcome to my webpage!</h1>")
file.write("</body>")
file.write("</html>")

# Close the file
file.close()

print("HTML file successfully written.")