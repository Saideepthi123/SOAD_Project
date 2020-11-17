import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:http/http.dart';
import 'package:provider/provider.dart';
import 'package:travel/APIcalls/ServerCalls.dart';
import 'package:travel/Models/City.dart';
import 'package:travel/Models/User.dart';
import 'package:travel/Screens/guidesTab.dart';
import 'package:travel/Screens/visitTab.dart';
import 'package:travel/Tools/Global%20tools.dart';

class CityPage extends StatefulWidget {
  @override
  _CityPageState createState() => _CityPageState();
}

class _CityPageState extends State<CityPage> with SingleTickerProviderStateMixin{
  TabController _tabController;

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
    final cityModel=Provider.of<City>(context);
    print(userModel.token);
    return Scaffold(
      appBar: TopAppBar(context),
      body: Container(
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            FutureBuilder(
              future: DataService.getCities(userModel.token),
              builder: (context, snapshot) {
                Response response=snapshot.data;
                // print(response.body);
                return Material(
                  elevation: 10,
                  child: Container(
                    decoration: BoxDecoration(
                        color: Colors.blueAccent,
                        image: DecorationImage(
                            image: AssetImage("img/ImageDelhi.jpg"),
                            fit: BoxFit.fill)),
                    width: _screenSize.width * 0.4,
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.end,
                      children: [Text("City Name",style: GoogleFonts.raleway(
                        fontSize: 30,color: Colors.white
                      ),), Text("City Info",style: GoogleFonts.raleway(
                          fontSize: 30,color: Colors.white
                      ),),
                      Padding(padding: EdgeInsets.all(20),)],
                    ),
                  ),
                );
              }
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
                    height: _screenSize.height*0.8,
                    width: _screenSize.width*0.6,
                    child: TabBarView(
                      controller: _tabController,
                      children: [
                        VisitTab(),
                        GuidesTab(),
                        Icon(Icons.fastfood,size: 80,),
                        Icon(Icons.emoji_transportation,size: 80,),
                        Icon(Icons.hotel,size: 80,)
                      ],
                    ),
                  )
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
