import 'package:flutter/material.dart';
import 'package:travel/Models/City.dart';
import 'package:travel/Screens/guidesTab.dart';
import 'package:travel/Screens/monumentInfoTabb.dart';
import 'package:travel/Tools/Global%20tools.dart';


class MonumentPage extends StatefulWidget {
  @override
  _MonumentPageState createState() => _MonumentPageState();
}

class _MonumentPageState extends State<MonumentPage> with SingleTickerProviderStateMixin{
  TabController _tabController;
  Monument monument = Monument.fromJSON({
    "monument_name": "Gateway Of India",
    "city_name": "Mumbai",
    "state": "Maharashtra",
    "country": "India",
    "city_id": "3",
    "basic_info": "The Gateway of India is an arch-monument built in the early twentieth century in the city of Mumbai, in the Indian state of Maharashtra. It was erected to commemorate the landing in December 1911 at Apollo Bunder, Mumbai of King-Emperor George V and Queen-Empress Mary, the first British monarch to visit India.",
    "imageURL": "https://www.travelogyindia.com/images/mumbai/gateway-of-india-tipl-1.jpg"
  });

  @override
  void initState() {
    super.initState();
    _tabController = TabController(vsync: this, length: 4);
  }

  @override
  Widget build(BuildContext context) {
    final _tabKey= UniqueKey();
    var _screenSize = MediaQuery.of(context).size;
    return Scaffold(
      appBar: TopAppBar(context),
      body: Container(
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Material(
              elevation: 10,
              child: Container(
                decoration: BoxDecoration(
                    color: Colors.blueAccent,
                    image: DecorationImage(
                      image: NetworkImage(monument.imageURL),
                      fit: BoxFit.cover,
                    )),
                width: _screenSize.width * 0.4,
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.end,
                  children: [
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
                        Tab(text: "Info"),
                        Tab(text: "Guides"),
                        Tab(text: "Food"),
                        Tab(text: "Travel"),
                      ],
                    ),
                  ),
                  Container(
                    height: _screenSize.height*0.8,
                    width: _screenSize.width*0.6,
                    child: TabBarView(
                      controller: _tabController,
                      children: [
                        MonumentInfoTab(),
                        GuidesTab(),
                        Icon(Icons.fastfood,size: 80,),
                        Icon(Icons.emoji_transportation,size: 80,),
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
