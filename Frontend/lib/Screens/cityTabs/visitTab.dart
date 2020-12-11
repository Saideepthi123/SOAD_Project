import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:http/http.dart';
import 'package:provider/provider.dart';
import 'package:travel/APIcalls/ServerCalls.dart';
import 'package:travel/Models/City.dart';
import 'package:travel/Models/Monument.dart';
import 'package:travel/Models/User.dart';
import 'package:travel/Screens/City.dart';
import 'package:travel/Screens/Monument.dart';
import 'package:travel/Tools/Global%20tools.dart';

class VisitTab extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    final _screenSize = MediaQuery.of(context).size;
    final userModel = Provider.of<User>(context);
    final cityModel = Provider.of<City>(context);
    return Container(
      padding: EdgeInsets.all(20),
      child: Column(
        children: [
          //  search bar
          SearchBar(
            width: _screenSize.width * 0.4,
            onChange: (val) {
              print(val);
            },
          ),
          Padding(
            padding: EdgeInsets.all(_screenSize.height * 0.01),
          ),
          //  cards
          FutureBuilder<Object>(
              future: DataService.getMonumentFromCity(
                  userModel.token, cityModel.cityID),
              builder: (context, snapshot) {
                if (snapshot.connectionState == ConnectionState.done) {
                  if (snapshot.hasData) {
                    Response response = snapshot.data;
                    if (response.statusCode == 200) {
                      List data = jsonDecode(response.body);
                      return Container(
                        height: _screenSize.height * 0.6,
                        child: ListView.separated(
                          shrinkWrap: true,
                          itemCount: data.length,
                          separatorBuilder: (context, idx) {
                            return Padding(
                              padding: EdgeInsets.all(10),
                            );
                          },
                          itemBuilder: (context, idx) {
                            BasicMonument basicMonument =
                                BasicMonument.fromJSON(data[idx]);
                            return InkWell(
                              onTap: () {
                                // monument.populatefromJSON(json);
                                Navigator.push(
                                    context,
                                    MaterialPageRoute(
                                        builder: (context) => MonumentPage(
                                              monIdx: basicMonument.monumentID,
                                            )));
                              },
                              child: Card(
                                elevation: 10,
                                child: Container(
                                  height: _screenSize.height * 0.3,
                                  padding: EdgeInsets.all(10),
                                  child: Row(
                                    children: [
                                      Image.network(
                                        basicMonument.imageURL,
                                        fit: BoxFit.fill,
                                        loadingBuilder: (BuildContext context,
                                            Widget child,
                                            ImageChunkEvent loadingProgress) {
                                          if (loadingProgress == null)
                                            return child;
                                          return Center(
                                            child: CircularProgressIndicator(
                                              value: loadingProgress
                                                          .expectedTotalBytes !=
                                                      null
                                                  ? loadingProgress
                                                          .cumulativeBytesLoaded /
                                                      loadingProgress
                                                          .expectedTotalBytes
                                                  : null,
                                            ),
                                          );
                                        },
                                      ),
                                      Flexible(
                                        child: Container(
                                          padding: EdgeInsets.all(8),
                                          child: Column(
                                            crossAxisAlignment:
                                                CrossAxisAlignment.start,
                                            mainAxisAlignment:
                                                MainAxisAlignment.spaceEvenly,
                                            children: [
                                              Flexible(
                                                  child: Text(
                                                basicMonument.monumentName,
                                                overflow: TextOverflow.ellipsis,
                                                style: TextStyle(fontSize: 30),
                                              )),
                                              Flexible(
                                                  child: Text(
                                                basicMonument.basicInfo,
                                                style: TextStyle(fontSize: 15),
                                              )),
                                            ],
                                          ),
                                        ),
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                            );
                          },
                        ),
                      );
                    }
                  } else {
                    return Container(
                      child: Text("404Page Not Found"),
                    );
                  }
                }
                return Center(
                    child: Image.asset(
                  "monumentLoading.gif",
                  height: _screenSize.height * 0.3,
                  width: _screenSize.height * 0.3,
                  colorBlendMode: BlendMode.softLight,
                  // color: Colors.white,
                ));
              })
        ],
      ),
    );
  }
}
