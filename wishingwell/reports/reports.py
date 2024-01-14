#reports.py

def robots_report(title,request_code,request_reason,page_contents):
    with open(f"{title} robots.txt","w") as file:
        file.write(f"DOCUMENT TITLE = {title} robots.txt report\n\n")
        file.write(f"REQUEST CODE = {request_code}\n\n")
        file.write(f"REQUEST REASON = {request_reason}\n\n")
        file.write(f"\n\n*  *  *  *  *  *\n\nCODE RETRIEVED:\n\n*  *  *  *  *  *\n\n\n\n")
        file.write(f"\n\n{page_contents}\n\n")
        file.write(f"\n\n*  *  *  *  *  *\n\nEND OF DOCUMENT.\n\n*  *  *  *  *  *")


def scrape_report(title,request_code,request_reason,page_contents):
    with open(f"{title} scrape report.txt","w") as file:
        file.write(f"DOCUMENT TITLE = {title} web scraping session report\n\n")
        file.write(f"REQUEST CODE = {request_code}\n\n")
        file.write(f"REQUEST REASON = {request_reason}\n\n")
        file.write(f"\n\n*  *  *  *  *  *\n\nCODE RETRIEVED:\n\n*  *  *  *  *  *\n\n\n\n")
        file.write(f"\n\n{page_contents}\n\n")
        file.write(f"\n\n\n\n*  *  *  *  *  *\n\nEND OF DOCUMENT.\n\n*  *  *  *  *  *")

#End of reports.py