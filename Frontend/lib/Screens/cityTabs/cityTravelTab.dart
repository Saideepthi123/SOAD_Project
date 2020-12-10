import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart';
import 'package:provider/provider.dart';
import 'package:travel/APIcalls/ServerCalls.dart';
import 'package:travel/Models/City.dart';
import 'package:travel/Models/Travel.dart';
import 'package:travel/Models/User.dart';


class CityTravelTab extends StatefulWidget {
  @override
  _CityTravelTabState createState() => _CityTravelTabState();
}

class _CityTravelTabState extends State<CityTravelTab> {
  bool isSearch = false;
  DateTime depDate;
  TextEditingController _originC = TextEditingController();
  TextEditingController _destC = TextEditingController();
  @override
  Widget build(BuildContext context) {
    final user = Provider.of<User>(context);
    final cityModel = Provider.of<City>(context);
    final _screenSize = MediaQuery.of(context).size;
    return Container(
      padding: EdgeInsets.all(10),
      child: Column(
        // shrinkWrap: true,
        children: [
          Card(
            elevation: 10,
            child: Container(
              height: _screenSize.height * 0.1,
              // alignment: Alignment.topRight,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Container(
                    padding: EdgeInsets.all(8),
                    width: _screenSize.width * 0.2,
                    child: TextField(
                      controller: _originC,
                      decoration: InputDecoration(
                          labelText: "Origin",
                          border: OutlineInputBorder(
                            borderSide:
                                BorderSide(color: Colors.red, width: 5.0),
                          )),
                    ),
                  ),
                  Container(
                    padding: EdgeInsets.all(8),
                    width: _screenSize.width * 0.2,
                    child: TextField(
                      controller: _destC,
                      decoration: InputDecoration(
                        border: OutlineInputBorder(
                          borderSide: BorderSide(color: Colors.red, width: 5.0),
                        ),
                        labelText: 'Destination',
                      ),
                    ),
                  ),
                  FlatButton(
                    padding: EdgeInsets.all(8),
                    height: _screenSize.height * 0.1,
                    child: Row(
                      children: [
                        Text("Departure Date: "),
                        Icon(Icons.calendar_today_outlined),
                      ],
                    ),
                    onPressed: () {
                      showDatePicker(
                              context: context,
                              initialDate: DateTime.now(),
                              firstDate: DateTime.now(),
                              lastDate: DateTime(2022))
                          .then((date) {
                        if (date != null) {
                          setState(() {
                            depDate = date;
                          });
                          print(date);
                        }
                      });
                    },
                  ),
                  IconButton(
                    icon: Icon(Icons.search),
                    onPressed: () {
                      setState(() {
                        isSearch = true;
                      });
                    },
                  )
                ],
              ),
            ),
          ),
          isSearch
              ? Container(
                  padding: EdgeInsets.all(20),
                  child: FutureBuilder(
                    future: DataService.searchFlights(
                        user.token, _originC.text, _destC.text, depDate),
                    builder: (context, snapshot) {
                      if (snapshot.connectionState == ConnectionState.done) {
                        if (snapshot.hasData) {
                          Response response = snapshot.data;
                          print(response.body);
                          if (response.statusCode == 200) {
                            List data = jsonDecode(response.body);
                            print(data);
                            return ListView.builder(
                              shrinkWrap: true,
                              itemCount: data.length,
                              itemBuilder: (context, idx) {
                                Flight flight = Flight.fromJSON(data[idx]);
                                return Card(
                                  elevation: 10,
                                  shape: RoundedRectangleBorder(
                                      borderRadius: BorderRadius.circular(20)),
                                  child: Container(
                                      height: _screenSize.height * 0.2,
                                      padding: EdgeInsets.all(20),
                                      child: Row(
                                        mainAxisSize: MainAxisSize.min,
                                        crossAxisAlignment:
                                            CrossAxisAlignment.center,
                                        mainAxisAlignment:
                                            MainAxisAlignment.spaceEvenly,
                                        children: [
                                          Icon(
                                            Icons.flight_takeoff_rounded,
                                            size: 70,
                                            color:
                                                Theme.of(context).accentColor,
                                          ),
                                          Column(
                                            mainAxisAlignment:
                                                MainAxisAlignment.spaceEvenly,
                                            crossAxisAlignment:
                                                CrossAxisAlignment.start,
                                            mainAxisSize: MainAxisSize.max,
                                            children: [
                                              RichText(
                                                text: TextSpan(
                                                  text: 'Carrier : ',
                                                  style: TextStyle(
                                                      color: Theme.of(context)
                                                          .primaryColor),
                                                  children: <TextSpan>[
                                                    TextSpan(
                                                      text: flight.carrierName,
                                                      style: TextStyle(
                                                          color: Theme.of(
                                                                  context)
                                                              .primaryColor),
                                                    ),
                                                  ],
                                                ),
                                              ),
                                              RichText(
                                                text: TextSpan(
                                                  text: 'Price(INR) : ',
                                                  style: TextStyle(
                                                      color: Theme.of(context)
                                                          .primaryColor),
                                                  children: <TextSpan>[
                                                    TextSpan(
                                                      text: flight.minPrice
                                                          .toString(),
                                                      style: TextStyle(
                                                          color: Theme.of(
                                                                  context)
                                                              .primaryColor),
                                                    ),
                                                  ],
                                                ),
                                              ),
                                              Row(
                                                children: [
                                                  Text(
                                                    "Direct Flight : ",
                                                    style: TextStyle(
                                                        color: Theme.of(context)
                                                            .primaryColor),
                                                  ),
                                                  flight.direct
                                                      ? Icon(
                                                          Icons.check,
                                                          color: Colors.green,
                                                          size: 20,
                                                        )
                                                      : Icon(
                                                          Icons.wrong_location,
                                                          color: Colors.red,
                                                          size: 20,
                                                        )
                                                ],
                                              ),
                                              RichText(
                                                text: TextSpan(
                                                  text: 'Departure Date : ',
                                                  style: TextStyle(
                                                      color: Theme.of(context)
                                                          .primaryColor),
                                                  children: <TextSpan>[
                                                    TextSpan(
                                                      text: flight
                                                              .departureDate.day
                                                              .toString() +
                                                          ' / ',
                                                      style: TextStyle(
                                                          color: Theme.of(
                                                                  context)
                                                              .primaryColor),
                                                    ),
                                                    TextSpan(
                                                      text: flight.departureDate
                                                              .month
                                                              .toString() +
                                                          ' / ',
                                                      style: TextStyle(
                                                          color: Theme.of(
                                                                  context)
                                                              .primaryColor),
                                                    ),
                                                    TextSpan(
                                                      text: flight
                                                          .departureDate.year
                                                          .toString(),
                                                      style: TextStyle(
                                                          color: Theme.of(
                                                                  context)
                                                              .primaryColor),
                                                    ),
                                                  ],
                                                ),
                                              )
                                            ],
                                          ),
                                        ],
                                      )),
                                );
                              },
                            );
                          }
                        }
                        if (snapshot.hasError) {
                          return Container(
                            child: Text("404 Page Not Found"),
                          );
                        }
                      }
                      return Center(
                          child: Image.asset(
                        "flightLoading.gif",
                        height: _screenSize.height * 0.4,
                        width: _screenSize.height * 0.4,
                      ));
                      ;
                    },
                  ),
                )
              : Container()
        ],
      ),
    );
  }
}
