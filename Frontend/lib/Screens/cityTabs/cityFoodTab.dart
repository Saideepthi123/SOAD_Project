import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:http/http.dart';
import 'package:provider/provider.dart';
import 'package:travel/APIcalls/ServerCalls.dart';
import 'package:travel/Models/City.dart';
import 'package:travel/Models/Food.dart';
import 'package:travel/Models/User.dart';
import 'package:travel/Tools/Global%20tools.dart';
import 'package:url_launcher/url_launcher.dart';

class CityFoodTab extends StatefulWidget {
  @override
  _CityFoodTabState createState() => _CityFoodTabState();
}

class _CityFoodTabState extends State<CityFoodTab> {
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
      padding: EdgeInsets.all(10),
      child: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              SearchBar(
                width: _screenSize.width * 0.5,
                onChange: _onChanged,
              ),
              FlatButton(
                onPressed: ()async {
                  String zomatoURL='https://www.zomato.com';
                  await _launchInBrowser(zomatoURL);
                },
                child: Image.asset(
                  'img/zomato.png',
                  width: _screenSize.width * 0.1,
                  height: _screenSize.height*0.1,
                  fit: BoxFit.contain,
                ),
              )
            ],
          ),
          Padding(
            padding: EdgeInsets.all(_screenSize.height * 0.01),
          ),
          FutureBuilder(
            future: DataService.getFood(userModel.token, cityModel.cityName),
            builder: (context, snapshot) {
              if (snapshot.connectionState == ConnectionState.done) {
                if (snapshot.hasData) {
                  Response response = snapshot.data;
                  if (response.statusCode == 200) {
                    var jsonRest = jsonDecode(response.body);
                    List rests = jsonRest["restaurants"];
                    print(rests);
                    return Container(
                      height: _screenSize.height * 0.6,
                      width: _screenSize.width*0.5,
                      // width: _screenSize.width * 0.4,
                      child: ListView.builder(
                        shrinkWrap: true,
                        itemCount: rests.length,
                        physics: ClampingScrollPhysics(),
                        itemBuilder: (context, idx) {
                          Restaurant rest = Restaurant.fromJSON(rests[idx]);
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
                                    FadeInImage.assetNetwork(
                                      placeholder: "assets/loading.gif",
                                      image: rest.thumbImg != null
                                          ? rest.thumbImg
                                          : "No image",
                                      width: _screenSize.width * 0.1,
                                      height: _screenSize.width * 0.1,
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
                                                    "Cuisines : "
                                                  ),
                                                  Text(
                                                    rest.cuisines,
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
                                                    rest.cost2.toString(),
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
                                                      'Zomato',
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
