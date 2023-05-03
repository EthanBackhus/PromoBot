import os
from openpyxl import Workbook

async def createExcelFile():
    # Get the current directory of the script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create a new workbook
    workbook = Workbook()
    
    # Get the active worksheet
    worksheet = workbook.active
    
    # Write some data to the worksheet
    worksheet['A1'] = 'Hello'
    worksheet['B1'] = 'World'
    
    # Save the workbook to a file in the same directory as the script
    filename = os.path.join(current_dir, 'example.xlsx')
    workbook.save(filename)
    
    # Close the workbook
    workbook.close()
