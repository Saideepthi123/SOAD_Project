import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:consumerapp1/Models/City.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:consumerapp1/ServerCalls.dart';
import 'package:http/http.dart';
import 'package:consumerapp1/Tools.dart';
import 'guidesTab.dart';

import 'Models/City.dart';

class CityPage extends StatefulWidget {
  int cityIdx;
  CityPage({this.cityIdx});
  @override
  _CityPageState createState() => _CityPageState();
}

class _CityPageState extends State<CityPage> {
  int _selectedIndex=0;

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  Widget _widgetSelect(int _idx){
    final _screenSize=MediaQuery.of(context).size;
    switch(_idx){
      case 0: {
        return Icon(Icons.details);
        // return Material(
        //   elevation: 10,
        //   child: Container(
        //     decoration: BoxDecoration(
        //         color: Colors.blueAccent,
        //         image: DecorationImage(
        //             image:
        //             NetworkImage(
        //               city.imageURL,
        //             ),
        //             fit: BoxFit.fill)
        //     ),
        //     width: _screenSize.width,
        //     child: Column(
        //       mainAxisAlignment: MainAxisAlignment.end,
        //       children: [
        //         Text(city.cityName,
        //           style: GoogleFonts.raleway(
        //               fontSize: 30, color: Colors.white
        //           ),),
        //         Text(city.basicInfo,
        //           style: GoogleFonts.raleway(
        //               fontSize: 30, color: Colors.white
        //           ),),
        //         Padding(padding: EdgeInsets.all(20),)
        //       ],
        //     ),
        //   ),
        // );
      }
      case 1: {
        return Icon(Icons.location_city);
        // return Container(
        //   padding: EdgeInsets.all(20),
        //   child: Column(
        //     children: [
        //       //  search bar
        //       SearchBar(
        //         width: _screenSize.width * 0.4,
        //         onChange: (val) {
        //           print(val);
        //         },
        //       ),
        //       Padding(
        //         padding: EdgeInsets.all(_screenSize.height * 0.01),
        //       ),
        //       //  cards
        //       FutureBuilder<Object>(
        //           future:
        //           // DataService.getMonumentFromCity(userModel.token, city.cityID),
        //           builder: (context, snapshot) {
        //             if (snapshot.connectionState == ConnectionState.done) {
        //               if (snapshot.hasData) {
        //                 Response response = snapshot.data;
        //                 if (response.statusCode == 200) {
        //                   List data = jsonDecode(response.body);
        //                   return Container(
        //                     height: _screenSize.height * 0.6,
        //                     child: ListView.separated(
        //                       shrinkWrap: true,
        //                       itemCount: data.length,
        //                       separatorBuilder: (context, idx) {
        //                         return Padding(
        //                           padding: EdgeInsets.all(10),
        //                         );
        //                       },
        //                       itemBuilder: (context, idx) {
        //                         BasicMonument basicMonument =
        //                         BasicMonument.fromJSON(data[idx]);
        //                         return InkWell(
        //                           onTap: () {
        //                           //  show full data somehow
        //                           },
        //                           child: Card(
        //                             elevation: 10,
        //                             child: Container(
        //                               height: _screenSize.height * 0.3,
        //                               padding: EdgeInsets.all(10),
        //                               child: Row(
        //                                 children: [
        //                                   Image.network(
        //                                     basicMonument.imageURL,
        //                                     fit: BoxFit.fill,
        //                                     loadingBuilder: (BuildContext context,
        //                                         Widget child,
        //                                         ImageChunkEvent loadingProgress) {
        //                                       if (loadingProgress == null)
        //                                         return child;
        //                                       return Center(
        //                                         child: CircularProgressIndicator(
        //                                           value: loadingProgress
        //                                               .expectedTotalBytes !=
        //                                               null
        //                                               ? loadingProgress
        //                                               .cumulativeBytesLoaded /
        //                                               loadingProgress
        //                                                   .expectedTotalBytes
        //                                               : null,
        //                                         ),
        //                                       );
        //                                     },
        //                                   ),
        //                                   Flexible(
        //                                     child: Container(
        //                                       padding: EdgeInsets.all(8),
        //                                       child: Column(
        //                                         crossAxisAlignment:
        //                                         CrossAxisAlignment.start,
        //                                         mainAxisAlignment:
        //                                         MainAxisAlignment.spaceEvenly,
        //                                         children: [
        //                                           Flexible(
        //                                               child: Text(
        //                                                 basicMonument.monumentName,
        //                                                 overflow: TextOverflow.ellipsis,
        //                                                 style: TextStyle(fontSize: 30),
        //                                               )),
        //                                           Flexible(
        //                                               child: Text(
        //                                                 basicMonument.basicInfo,
        //                                                 style: TextStyle(fontSize: 15),
        //                                               )),
        //                                         ],
        //                                       ),
        //                                     ),
        //                                   ),
        //                                 ],
        //                               ),
        //                             ),
        //                           ),
        //                         );
        //                       },
        //                     ),
        //                   );
        //                 }
        //               } else {
        //                 return Container(
        //                   child: Text("404Page Not Found"),
        //                 );
        //               }
        //             }
        //             return Center(
        //                 child: CircularProgressIndicator());
        //           })
        //     ],
        //   ),
        // );
      }
      case 2: {
        return GuidesTab();
      }
    }
  }
  @override
  Widget build(BuildContext context) {
    final _screenSize=MediaQuery.of(context).size;
    return Scaffold(
      appBar: AppBar(
        title: Text("Mumbai"),
      ),
      body: Container(
        child:
        // FutureBuilder(
        //   future: ,
          // future: DataService.getCity(api_key,widget.cityIdx),
          // builder: (context,snapshot){
          //   if(snapshot.connectionState==ConnectionState.done){
          //     if(snapshot.hasData){
          //       Response response= snapshot.data;
          //       print(response.statusCode);
          //       if(response.statusCode==200) {
          //         Response response = snapshot.data;
          //         Map<String,dynamic> json=jsonDecode(response.body);
          //         print("city:: "+json.toString());
          //         print(response.body);
          //         City city= City.fromJSON(json);
          //         return
      _widgetSelect(_selectedIndex),
    // ;
    //             }
    //             else{
    //               return Container(
    //                 child: Text("With Response: 404 Page Not Found"),
    //               );
    //             }
    //           }
    //           if(snapshot.hasError){
    //             return Container(
    //               child: Text("404 Page Not Found"),
    //             );
    //           }
    //         }
    //         return Center(
    //             child: Image.asset(
    //               "pageLoading.gif",
    //               height: _screenSize.height*0.9,
    //               width: _screenSize.height*0.9,
    //             )
    //         );
    //       },
        // ),
        // _widgetSelect(_selectedIndex),
      // ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.drive_file_rename_outline),
            label: 'Info',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.location_city),
            label: 'Monuments',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.people),
            label: 'Guides',
          ),
        ],
        currentIndex: _selectedIndex,
        selectedItemColor: Colors.amber[800],
        onTap: _onItemTapped,
      ),
    );
  }
}
