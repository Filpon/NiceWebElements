from bs4 import BeautifulSoup


class BeautifulSoupWorksWithSite:
    """
    Class for working with Site via BeautifulSoup
    """

    def __init__(self, html):
        self.soup = BeautifulSoup(html, "html.parser")

    def parse_tables(self) -> list:
        """
        Parsing data from web table
        :return: Parsed list with excel rows
        """
        try:
            rows_for_excel = []
            current_table = self.soup.find("table", {"class": "tablels"})
            table_rows = current_table.find_all(["th", "td"])
            counter = 0
            row_in_excel = []
            for row in table_rows:
                row_in_excel.append(row.text)
                counter += 1
                if counter == 3:
                    rows_for_excel.append(row_in_excel)
                    counter = 0
                    row_in_excel = []
            return rows_for_excel
        except Exception:
            return []
