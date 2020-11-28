import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:http/http.dart';
import 'package:provider/provider.dart';
import 'package:travel/APIcalls/ServerCalls.dart';
import 'package:travel/Models/City.dart';
import 'package:travel/Models/Food.dart';
import 'package:travel/Models/Hotels.dart';
import 'package:travel/Models/User.dart';
import 'package:travel/Tools/Global%20tools.dart';

class CityHotelTab extends StatefulWidget {
  @override
  _CityHotelTabState createState() => _CityHotelTabState();
}

class _CityHotelTabState extends State<CityHotelTab> {
  String cityName;

  _onChanged(String val) {
    setState(() {
      cityName = val;
    });
  }

  @override
  Widget build(BuildContext context) {
    final _screenSize = MediaQuery.of(context).size;
    final cityModel = Provider.of<City>(context);
    final userModel = Provider.of<User>(context);
    return Container(
      child: Column(
        children: [
          SearchBar(
            width: _screenSize.width * 0.3,
            onChange: _onChanged,
          ),
          FutureBuilder(
            future: DataService.getHotels(userModel.token, cityModel.cityName),
            builder: (context, snapshot) {
              if (snapshot.connectionState == ConnectionState.done) {
                if (snapshot.hasData) {
                  Response response = snapshot.data;
                  print(response.statusCode.toString()+"He is here now");
                  if (response.statusCode == 200) {
                    List jsonRest = jsonDecode(response.body);
                    return Container(
                      height: _screenSize.height * 0.7,
                      width: _screenSize.width * 0.4,
                      child: ListView.builder(
                        shrinkWrap: true,
                        itemCount: jsonRest.length,
                        physics: ClampingScrollPhysics(),
                        itemBuilder: (context, idx) {
                          Hotels rest = Hotels.fromJson(jsonRest[idx]);
                          return Card(
                            elevation: 10,
                            shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(20)),
                            child: Container(
                                height: _screenSize.height * 0.2,
                                padding: EdgeInsets.all(20),
                                child: Row(
                                  // mainAxisSize: MainAxisSize.min,
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  // mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                                  children: [
                                    FadeInImage.assetNetwork(
                                      placeholder: "assets/loading.gif",
                                      image: rest.visitUrl != null
                                          ? rest.visitUrl
                                          : "No image",
                                      width: _screenSize.width * 0.3,
                                      height: _screenSize.width * 0.3,
                                    ),
                                    Flexible(
                                      child: Container(
                                        width: _screenSize.width * 0.6,
                                        child: Column(
                                          mainAxisAlignment:
                                              MainAxisAlignment.spaceEvenly,
                                          crossAxisAlignment:
                                              CrossAxisAlignment.start,
                                          mainAxisSize: MainAxisSize.max,
                                          children: [
                                            Text(
                                              rest.name,
                                              overflow: TextOverflow.ellipsis,
                                              style: TextStyle(
                                                  color: Theme.of(context)
                                                      .primaryColor),
                                              softWrap: false,
                                            ),
                                          ],
                                        ),
                                      ),
                                    ),
                                  ],
                                )),
                          );
                        },
                      ),
                    );
                  } else {
                    return Container(
                      child: Text("404: Page Not Found"),
                    );
                  }
                } else {
                  return Container(
                    child: Text("404: Page Not Found"),
                  );
                }
              }
              return Container(
                child: Center(child: CircularProgressIndicator()),
              );
            },
          )
        ],
      ),
    );
  }
}
