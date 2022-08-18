

class GaugeData:

    @staticmethod
    def table_to_dict(table):
        """
        Parsing method for a table with two columnts

        |User_Information|Value|
        |----------------|-------|
        |first_name      |Andrei |

        """

        return dict(zip([str(elem) for elem in table.get_column_values_with_name(table.headers[0])],
                        [str(elem) for elem in table.get_column_values_with_name(table.headers[1])]
                        ))
