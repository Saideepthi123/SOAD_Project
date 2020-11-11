import 'package:flutter/material.dart';
import 'package:travel/Screens/guidesTab.dart';
import 'package:travel/Tools/Global%20tools.dart';


class MonumentPage extends StatefulWidget {
  @override
  _MonumentPageState createState() => _MonumentPageState();
}

class _MonumentPageState extends State<MonumentPage> with SingleTickerProviderStateMixin{
  TabController _tabController;

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
                        image: AssetImage("img/ImageDelhi.jpg"),
                        fit: BoxFit.fill)),
                width: _screenSize.width * 0.4,
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [Text("City Name"), Text("City Info")],
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
                        Icon(Icons.receipt_long,size: 80,),
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
