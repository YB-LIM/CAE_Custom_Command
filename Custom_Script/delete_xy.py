from abaqus import session

def delete_xy():
    # Get the names of all XYData objects in the current session
    xy_data_names = session.xyDataObjects.keys()

    # Loop through each XYData object name and delete it
    for name in xy_data_names:
        del session.xyDataObjects[name]

    print("All XYData objects have been deleted.")
