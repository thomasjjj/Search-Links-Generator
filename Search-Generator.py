import urllib.parse
import tkinter as tk
import webbrowser

'''
This python tool takes an input of words as search terms and generates useful links for each ter.
Search terms can have multiple words in them and are each on their own line.

WARNING: This tool opens links in the default browser. If there are any OPSEC issues please consider that this tool
will open those links with the account currently logged in on that browser. 
'''

# Define the base URLs for each search engine
facebook_base_url = "https://www.facebook.com/search/top/?q="
twitter_base_url = "https://twitter.com/search?q="
vk_base_url = "https://vk.com/search?c%5Bq%5D="
google_base_url = "https://www.google.com/search?q="
yandex_base_url = "https://yandex.com/search/?text="

# Define a function to generate links for each search engine for the entered search terms
def generate_links():
    # Get the search terms from the text box
    search_terms = text_box.get("1.0", "end").strip().split("\n")

    # Create an HTML file for displaying the generated links
    with open("search_links.html", "w", encoding="utf-8") as f:
        # Write the HTML header
        f.write("<html>\n<head>\n<title>Search Engine Links</title>\n</head>\n<body>\n")

        # Write the Page title
        f.write(
            "<h1>OSINT link generator.</h1>\n")

        # Write the subtitle explaining that links will open in the browser with the user's signed-in accounts
        f.write("<h2 style='color: red'>OPSEC Note: Links will open in the browser with your signed-in accounts. Please only click links if you are sure it is safe to do so.</h2>\n")

        # Generate links for each search engine for each search term and write them to the HTML file
        for term in search_terms:
            # Encode the search term for use in the URL
            encoded_term = urllib.parse.quote(term)

            # Generate the links for each search engine
            facebook_link = facebook_base_url + encoded_term
            twitter_link = twitter_base_url + encoded_term
            vk_link = vk_base_url + encoded_term
            google_link = google_base_url + encoded_term
            yandex_link = yandex_base_url + encoded_term

            # Write the links to the HTML file as clickable hyperlinks
            f.write(f"<p><strong>Search term: {term}</strong><br>\n")
            f.write(f"<a href='{facebook_link}' target='_blank' onclick='changeColor(this)'>Facebook</a> ")
            f.write(f"<a href='{twitter_link}' target='_blank' onclick='changeColor(this)'>Twitter</a> ")
            f.write(f"<a href='{vk_link}' target='_blank' onclick='changeColor(this)'>VK</a> ")
            f.write(f"<a href='{google_link}' target='_blank' onclick='changeColor(this)'>Google</a> ")
            f.write(f"<a href='{yandex_link}' target='_blank' onclick='changeColor(this)'>Yandex</a></p>\n")

        # Add a script to the HTML file that changes the color of the links to green when they are clicked
        f.write("<script>\n")
        f.write("function changeColor(link) {\n")
        f.write("  link.style.color = 'green';\n")
        f.write("}\n")
        f.write("</script>\n")

        # Write the HTML footer
        f.write("</body>\n</html>")

    # Open the HTML file in the default web browser
    webbrowser.open_new_tab("search_links.html")

# Create the GUI window
root = tk.Tk()
root.title("Search Engine Links Generator")

# Create the heading for the window
heading = tk.Label(root, text="Enter list of search terms, one on each row")
heading.pack()

# Create the text box for entering the search terms
text_box = tk.Text(root, height=10, width=50)
text_box.pack(side="left", fill="both", expand=True)

# Create the scrollbar for the text box
scrollbar = tk.Scrollbar(root, command=text_box.yview)
scrollbar.pack(side="right", fill="y")
text_box.config(yscrollcommand=scrollbar.set)

# Create the search button
search_button = tk.Button(root, text="Search", command=generate_links)
search_button.pack()



# Start the GUI event loop
root.mainloop()
