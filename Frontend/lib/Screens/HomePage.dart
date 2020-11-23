import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:travel/Models/Image.dart';
import 'package:travel/Screens/exploreCity.dart';
import 'package:travel/Tools/Global%20tools.dart';


class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen>
    with TickerProviderStateMixin {
  List _selected = List.generate(5, (index) => false);
  int prevVal = 0;
  // AuthService auth=AuthService();

  setSelected(int val) {
    if (prevVal != val) {
      setState(() {
        _selected[prevVal] = false;
        _selected[val] = true;
        prevVal = val;
      });
    }
  }
  Widget selectWidget() {
    switch (prevVal) {
      case 0:
        return ChangeNotifierProvider<BackImage>(
          create: (_) => BackImage(
              Container(
                decoration: BoxDecoration(
                    image: DecorationImage(
                        image: AssetImage('img/ImageDelhi.jpg'),
                        fit: BoxFit.cover)),
              ),
              "Delhi",
              "A city is a large human settlement"),
          child: ExploreWidget(),
        );
        //   Container(
        //     color: Colors.white,
        //     child: Text("Explore"),
        // );
      case 1:
        return Container(
          color: Colors.white,
          child: Text("Guides"),
        );
      case 2:
        return Container(
          color: Colors.white,
          child: Text("Bucket List"),
        );
      case 3:
        return Container(
          color: Colors.white,
          child: Text("History"),
        );
      // case 4:
        // return ProfileScreen();
      default:
        return Container(
          color: Colors.white,
          child: Text("No such page"),
        );
    }
  }

  bool isexpand = false;
  Animation<double> animation;
  AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _selected[0]=true;
    initiatingAnimations();
    expandController();
//    globals.populateReview();
  }

  void initiatingAnimations() {
    _controller =
        AnimationController(vsync: this, duration: Duration(milliseconds: 500));
    animation =
        CurvedAnimation(parent: _controller, curve: Curves.fastOutSlowIn);
  }

  void expandController() {
    setState(() {
      if (isexpand) {
        _controller.forward();
      } else {
        _controller.reverse();
      }
      isexpand = !isexpand;
    });
  }

  @override
  Widget build(BuildContext context) {
    final selCol = Theme.of(context).primaryColor.withOpacity(0.5);
    final notCol = Theme.of(context).accentColor.withOpacity(0.4);
    final _screensize = MediaQuery.of(context).size;
    return Scaffold(
      appBar: TopAppBar(context),
      body: Container(
        child: Row(
          children: [
            Container(
              width: _screensize.width * 0.15,
              color: Theme.of(context).backgroundColor,
              child: Column(
                children: [
                  Spacer(
                    flex: 1,
                  ),
                  InkWell(
                    onTap: (){
                      setSelected(0);
                    },
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.end,
                      children: [
                        AnimatedContainer(
                          height: 40,
                          duration: Duration(milliseconds: 300),
                          curve: Curves.easeIn,
                          color: Theme.of(context).accentColor,
                          width: _selected[0]?4:0,
                        ),
                        Container(
                          height: 40,
                          child: Row(
                            children: [
                              Padding(
                                padding: const EdgeInsets.only(left:20.0,right: 15.0),
                                child: Icon(Icons.explore),
                              ),
                              Text("Explore"),
                            ],
                          ),
                        )
                      ],
                    ),
                  ),
                  InkWell(
                    onTap: (){
                      setSelected(1);
                    },
                    child: Row(
                      children: [
                        AnimatedContainer(
                          height: 40,
                          duration: Duration(milliseconds: 300),
                          curve: Curves.easeIn,
                          color: Theme.of(context).accentColor,
                          width: _selected[1]?4:0,
                        ),
                        Container(
                          height: 40,
                          child: Row(
                            children: [
                              Padding(
                                padding: const EdgeInsets.only(left:20.0,right: 15.0),
                                child: Icon(Icons.people),
                              ),
                              Text("Guides")
                            ],
                          ),
                        )
                      ],
                    ),
                  ),
                  InkWell(
                    onTap: (){
                      setSelected(2);
                    },
                    child: Row(
                      children: [
                        AnimatedContainer(
                          height: 40,
                          duration: Duration(milliseconds: 300),
                          curve: Curves.easeIn,
                          color: Theme.of(context).accentColor,
                          width: _selected[2]?4:0,
                        ),
                        Container(
                          height: 40,
                          child: Row(
                            children: [
                              Padding(
                                padding: const EdgeInsets.only(left:20.0,right: 15.0),
                                child: Icon(Icons.favorite_sharp),
                              ),
                              Text("Bucket List")
                            ],
                          ),
                        )
                      ],
                    ),
                  ),
                  InkWell(
                    onTap: (){
                      setSelected(3);
                    },
                    child: Row(
                      children: [
                        AnimatedContainer(
                          height: 40,
                          duration: Duration(milliseconds: 300),
                          curve: Curves.easeIn,
                          color: Theme.of(context).accentColor,
                          width: _selected[3]?4:0,
                        ),
                        Container(
                          height: 40,
                          child: Row(
                            children: [
                              Padding(
                                padding: const EdgeInsets.only(left: 20.0,right: 15.0),
                                child: Icon(Icons.history_outlined),
                              ),
                              Text("History",),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ),
                  Spacer(
                    flex: 1,
                  ),
                ],
              ),
            ),
            selectWidget(),
          ],
        ),
      ),
    );
  }
}

