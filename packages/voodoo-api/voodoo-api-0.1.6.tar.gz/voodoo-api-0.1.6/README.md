#Voodoo API

## Example

    from voodooapi import API

    shipping_info = {
        "name": "Oliver Ortlieb",
        "street1": "320 2nd Ave",
        "street2": "#5",
        "city": "New York",
        "state": "NY",
        "zip": "10003",
        "country": "USA"
    }

    api_key = "your-api-key-goes-here"

    api = API(api_key)

    file_url = "https://mydomain.com/somefile.stl"
    qty = 1

    materials = api.get_materials()

    khaki = [m["color"] for m in materials if m["color"] == "Khaki"]

    material_id = khaki["id"]

    quote = api.upload_and_quote_model(file_url, qty, material_id, shipping_info)

    print "Price is $%.2f." % (quote["quote"]["total"])
    purchase = (raw_input("Would you like to complete the purchase? (y/n)").lower() == 'y')

    if purchase:
        order = api.confirm_order(quote["quote_id"])
        print order
        print "Purchase completed."


## Classes
## API


###API(api_key)

Creates an API instance that uses the given api key. You should provide a correct API key or the API will not work.

###API.get_materials()

Returns a list of available materials for printing.

Example response:

    # Truncated example showing the structure of the response
    [{u'color': u'True Red', u'type': u'PLA', u'id': 1},
     {u'color': u'True Brown', u'type': u'PLA', u'id': 2},
     ...]
    # End of response


###API.create_model(file_url):

Creates a model on the Voodoo servers representing the model provided by file_url. The Voodoo servers will download the file before providing a response.

Example response:

    {u'user_id': 1,
    u'deletedAt': None,
    u'file_uri':
    u'3c911686-4bbe-4fb7-b08e-354e88f1274b.stl',
    u'volume': 263703.684920517,
    u'updatedAt':u'2015-06-15T15:23:21.122Z',
    u'y': 63.9124984741211,
    u'x': 155.777496337891,
    u'z': 110.86499786377,
    u'id': 25,
    u'createdAt': u'2015-06-15T15:23:21.122Z'}

###API.create_order(order_items, shipping_info):
Creates an order request on the server and returns a quote for that order, along with a quote id used to confirm the order. The purchase is not completed until the confirm_order method is executed with the appropriate quote_id.

Example usage:

    # Order items is a list of dictionaries with the keys:
    # { "material": material_id, "id": model_id, "qty": number }
    order_items = {'material': 34, 'id': 25, 'qty': 1

    # Shipping info is a dictionary with the keys:
    shipping_info = {
        'city': 'Test city,
        'name': 'Test name',
        'zip': '12345',
        'street1': '123 Test Rd',
        'street2': '#1', # optional!
        'state': 'AK',
        'country': 'USA'
    }

    print API.create_order(order_items, shipping_info)
    # Response
    {
        u'quote':
            {u'items': 263814.55,
            u'total': 290196.01,
            u'tax': 26381.46,
            u'shipping': 0},
        u'quote_id': u'123456',
        u'shipping':
            {u'city': u'New York',
             u'name': u'Oliver Ortlieb',
             u'zip': u'10003',
             u'street1': u'320 2nd Ave',
             u'street2': u'#5',
             u'state': u'NY',
             u'country': u'USA'},
        u'order_items': [
            {u'material': 34, u'id': 25, u'qty': 1}
        ]
    }



###API.confirm_order(quote_id):
Confirms the order given by quote_id. Prior to calling this method, no order will be printed and no money will be charged.

Response is the same as create_order.

###API.upload_and_quote_model(file_url, qty, material, shipping_info):
Creates a model for file_url and quotes it for the given quantity, material, and target shipping address. Returns the same response as create_order.
