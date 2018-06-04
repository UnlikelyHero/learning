# Not working. too many variables?

kwargs = {
  "tracking_number": "439738830101",
  "status_code": "IT",
  "status_description": "In Transit",
  "carrier_status_code": "LO",
  "carrier_status_description": "In transit",
  "ship_date": "2018-04-25T07:00:00Z",
  "estimated_delivery_date": "2018-04-30T07:00:00Z",
  "actual_delivery_date": "null",
  "exception_description": "null",
  "events": [{
      "occurred_at": "2018-04-26T08:29:22Z",
      "description": "Left FedEx origin facility",
      "city_locality": "ROMEOVILLE",
      "state_province": "IL",
      "postal_code": "60446",
      "country_code": "US",
      "company_name": "null",
      "signer": "null"
    },
    {
      "occurred_at": "2018-04-26T05:40:00Z",
      "description": "Arrived at FedEx location",
      "city_locality": "ROMEOVILLE",
      "state_province": "IL",
      "postal_code": "60446",
      "country_code": "US",
      "company_name": "null",
      "signer": "null"
    },
    {
      "occurred_at": "2018-04-25T23:56:00Z",
      "description": "Picked up",
      "city_locality": "ROMEOVILLE",
      "state_province": "IL",
      "postal_code": "60446",
      "country_code": "US",
      "company_name": "null",
      "signer": "null"
    },
    {
      "occurred_at": "2018-04-25T15:17:00Z",
      "description": "Shipment information sent to FedEx",
      "city_locality": "null",
      "state_province": "null",
      "postal_code": "60504",
      "country_code": "US",
      "company_name": "null",
      "signer": "null"
    }
  ]
}

print(**kwargs)
