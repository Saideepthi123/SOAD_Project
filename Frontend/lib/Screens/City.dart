import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:http/http.dart';
import 'package:provider/provider.dart';
import 'package:travel/APIcalls/ServerCalls.dart';
import 'package:travel/Models/City.dart';
import 'package:travel/Models/User.dart';
import 'package:travel/Screens/cityTravelTab.dart';
import 'package:travel/Screens/guidesTab.dart';
import 'package:travel/Screens/visitTab.dart';
import 'package:travel/Tools/Global%20tools.dart';

class CityPage extends StatefulWidget {
  int cityIdx;
  CityPage({this.cityIdx});
  @override
  _CityPageState createState() => _CityPageState();
}

class _CityPageState extends State<CityPage> with SingleTickerProviderStateMixin{
  TabController _tabController;


  // Map<String,dynamic> json={
  //   "city_name": "Mumbai",
  //   "state": "Maharashtra",
  //   "country": "India",
  //   "pin_code": "400001",
  //   "city_id": 1,
  //   "imageURL": "abc.png",
  //   "monuments": [ ]
  // };

  @override
  void initState() {
    super.initState();
    _tabController = TabController(vsync: this, length: 5);
  }

  @override
  Widget build(BuildContext context) {
    final _tabKey= UniqueKey();
    var _screenSize = MediaQuery.of(context).size;
    final userModel=Provider.of<User>(context);
    // final cityModel=Provider.of<City>(context);
    print("city index" +widget.cityIdx.toString());
    print(userModel.token);
    return Scaffold(
      appBar: TopAppBar(context),
      body: FutureBuilder(
        future: DataService.getCity(userModel.token,widget.cityIdx),
        builder: (context,snapshot){
          if(snapshot.connectionState==ConnectionState.done){
            if(snapshot.hasData){
              Response response= snapshot.data;
              print(response.statusCode);
              if(response.statusCode==200) {
                Response response = snapshot.data;
                Map<String,dynamic> json=jsonDecode(response.body);
                print("city:: "+json.toString());
                print(response.body);
                return ChangeNotifierProvider(
                    create: (context) => City.fromJSON(json),
                    child: Container(
                      child: Consumer<City>(
                        builder: (context, city, child){
                          print(city.cityName);
                          print(city.country);
                          print(city.imageURL);
                          return Row(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Material(
                                elevation: 10,
                                child: Container(
                                  decoration: BoxDecoration(
                                      color: Colors.blueAccent,
                                      image: DecorationImage(
                                          image:
                                          NetworkImage(
                                              city.imageURL,
                                          ),
                                          fit: BoxFit.fill)
                                        ),
                                  width: _screenSize.width * 0.4,
                                  child: Column(
                                    mainAxisAlignment: MainAxisAlignment.end,
                                    children: [
                                      Text(city.cityName,
                                        style: GoogleFonts.raleway(
                                            fontSize: 30, color: Colors.white
                                        ),),
                                      Text(city.basicInfo,
                                        style: GoogleFonts.raleway(
                                            fontSize: 30, color: Colors.white
                                        ),),
                                      Padding(padding: EdgeInsets.all(20),)
                                    ],
                                  ),
                                ),
                              ),
                              DefaultTabController(
                                length: 5,
                                child: Column(
                                  children: [
                                    Container(
                                      color: Colors.orangeAccent,
                                      width: _screenSize.width * 0.6,
                                      child: TabBar(
                                        controller: _tabController,
                                        indicatorColor: Colors.white,
                                        tabs: [
                                          Tab(text: "Visit"),
                                          Tab(text: "Guides"),
                                          Tab(text: "Food"),
                                          Tab(text: "Travel"),
                                          Tab(text: "Stay"),
                                        ],
                                      ),
                                    ),
                                    Container(
                                      height: _screenSize.height * 0.8,
                                      width: _screenSize.width * 0.6,
                                      child: TabBarView(
                                        controller: _tabController,
                                        children: [
                                          VisitTab(),
                                          GuidesTab(),
                                          Icon(Icons.fastfood, size: 80,),
                                          CityTravelTab(),
                                          Icon(Icons.hotel, size: 80,)
                                        ],
                                      ),
                                    )
                                  ],
                                ),
                              ),
                            ],
                          );
                        }
                      ),
                    ));
              }
              else{
                return Container(
                  child: Text("With Response: 404 Page Not Found"),
                );
              }
            }
            if(snapshot.hasError){
              return Container(
                child: Text("404 Page Not Found"),
              );
            }
          }
          return Center(
              child: Image.asset(
                "pageLoading.gif",
                height: _screenSize.height*0.9,
                width: _screenSize.height*0.9,
              )
          );
        },
      ),
    );
  }
}
