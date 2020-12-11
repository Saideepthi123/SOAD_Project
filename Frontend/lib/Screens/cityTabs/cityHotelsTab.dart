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
import 'package:url_launcher/url_launcher.dart';

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
  Future<void> _launchInBrowser(String url) async {
    if (await canLaunch(url)) {
      await launch(
        url,
        forceSafariVC: false,
        forceWebView: false,
        headers: <String, String>{'my_header_key': 'my_header_value'},
      );
    } else {
      throw 'Could not launch $url';
    }
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
                                  mainAxisSize: MainAxisSize.min,
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  // mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                                  children: [
                                    Padding(
                                      padding: const EdgeInsets.all(10.0),
                                      child: FadeInImage.assetNetwork(
                                        placeholder: "assets/loading.gif",
                                        image: rest.visitUrl != null
                                            ? rest.visitUrl
                                            : "No image",
                                        width: _screenSize.width * 0.1,
                                        height: _screenSize.width * 0.1,
                                      ),
                                    ),
                                    Flexible(
                                      child: Container(
                                        width: _screenSize.width * 0.6,
                                        child: Column(
                                          mainAxisAlignment:
                                          MainAxisAlignment.spaceEvenly,
                                          crossAxisAlignment:
                                          CrossAxisAlignment.start,
                                          children: [
                                            Text(
                                              rest.name,
                                              overflow: TextOverflow.ellipsis,
                                              style: TextStyle(
                                                  color: Theme.of(context)
                                                      .primaryColor),
                                              softWrap: false,
                                            ),
                                            Flexible(
                                              child: Row(
                                                children: [
                                                  Text(
                                                      "Rating : "
                                                  ),
                                                  Text(
                                                    rest.ratings.toString(),
                                                    // overflow: TextOverflow.ellipsis,
                                                    style: TextStyle(
                                                        color: Theme.of(context)
                                                            .primaryColor),
                                                    softWrap: false,
                                                  ),
                                                ],
                                              ),
                                            ),
                                            Flexible(
                                              child: Row(
                                                children: [
                                                  Text(
                                                      "Cost for two : "
                                                  ),
                                                  Text(
                                                    rest.cost,
                                                    // overflow: TextOverflow.ellipsis,
                                                    style: TextStyle(
                                                        color: Theme.of(context)
                                                            .primaryColor),
                                                    softWrap: false,
                                                  ),
                                                  Text(
                                                    " INR",
                                                    style: TextStyle(
                                                        color: Theme.of(context)
                                                            .primaryColor),
                                                    softWrap: false,
                                                  ),
                                                ],
                                              ),
                                            ),
                                            Flexible(
                                              child: Row(
                                                children: [
                                                  Text(
                                                      "Order Now at "
                                                  ),
                                                  InkWell(
                                                    onTap: () async {
                                                      await _launchInBrowser(rest.visitUrl);
                                                    },
                                                    child: Text(
                                                      'Hotels',
                                                      // overflow: TextOverflow.ellipsis,
                                                      style: TextStyle(
                                                          color: Colors.red),
                                                      softWrap: false,
                                                    ),
                                                  ),
                                                ],
                                              ),
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
