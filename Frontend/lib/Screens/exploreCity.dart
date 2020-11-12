import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';
import 'package:travel/Models/Image.dart';
import 'package:travel/Screens/City.dart';
import 'package:travel/Tools/Global%20tools.dart';
import 'package:travel/Tools/ImageShifter.dart';

class ExploreWidget extends StatefulWidget {
  @override
  _ExploreWidgetState createState() => _ExploreWidgetState();
}

class _ExploreWidgetState extends State<ExploreWidget> {
  final _key = GlobalKey<AnimatedListState>();
  final myTween = Tween<Offset>(
    begin: const Offset(0.0, -1.0),
    end: Offset.zero,
  );

  @override
  Widget build(BuildContext context) {
    final _screensize = MediaQuery.of(context).size;
    var change = Provider.of<BackImage>(context);
    return Container(
      width: _screensize.width * 0.83,
      child: Row(
        children: [
          Container(
                  width: _screensize.width * 0.35,
                  decoration: BoxDecoration(
                    color: Colors.lightBlueAccent,
                    borderRadius: BorderRadius.only(
                      topRight: Radius.circular(20),
                      bottomRight: Radius.circular(20),
                    )
                  ),
                  child: Stack(
                    children: [
                      InkWell(
                        child: ImageShifter(
                          xOffset: 0.0,
                          yOffset: -1.0,
                        ),
                        onTap: (){
                          Navigator.push(context,MaterialPageRoute(builder: (context) => CityPage()));
                        },
                      ),
                      Container(
                        alignment: Alignment.center,
                        margin: EdgeInsets.only(left: 50),
                        child: AnimatedSwitcher(
                          duration: Duration(milliseconds: 700),
                          transitionBuilder:
                              (Widget child, Animation<double> animation) {
                            return SlideTransition(
                              child: child,
                              position: Tween<Offset>(
                                  begin: Offset(0.0, -1.0),
                                  end: Offset(0.0, 0.0))
                                  .animate(animation),
                            );
                          },
                          child: Container(
                            key: Key(change.cityname),
                            child: Column(
                              mainAxisAlignment: MainAxisAlignment.end,
                              children: [
                                Text(
                                  change.cityname,
                                  style: GoogleFonts.lato(
                                      color: Colors.white,
                                      fontSize: 52,
                                      fontWeight: FontWeight.w900),
                                ),
                                Text(change.metadata,
                                  style: GoogleFonts.lato(
                                      color: Colors.white,
                                      fontSize: 18,
                                      fontWeight: FontWeight.w500),
                                  overflow: TextOverflow.ellipsis,),
                                Padding(
                                  padding: EdgeInsets.all(20),
                                )
                              ],
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
          Container(
            width: _screensize.width * 0.48,
              padding: EdgeInsets.all(10),
              child: Column(
                children: [
                  SearchBar(
                    width: _screensize.width*0.45 - 30,
                    suggestions: [
                        "Italy",
                        "France",
                        "Russia",
                        "Japan"
                    ],
                    onChange: (val){
                      print(val);
                    },
                  ),
                  Padding(
                    padding: EdgeInsets.all(10),
                  ),
                  Container(
                    width: _screensize.width * 0.48,
                    height: _screensize.height * 0.7,
                    padding: EdgeInsets.all(10),
                    child: AnimatedList(
                        key: _key,
                        initialItemCount: change.cities.length,
                        itemBuilder: (context, index, animation) {
                          return SlideTransition(
                            position: animation.drive(myTween),
                            child: Card(
                              shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(20)),
                              elevation: 20,
                              color: Colors.blue,
                              margin: EdgeInsets.symmetric(horizontal: 20,vertical: 20),
                              child: InkWell(
                                onTap: () {
                                  change.currimage(change.cities[index]);
                                  change.cityname = change.cities[index];
                                  print(change.cities);
                                },
                                child: Container(
                                  decoration: BoxDecoration(
                                      image: DecorationImage(
                                          image: AssetImage('img/CardImage' +
                                              change.cities[index] +
                                              '.jpg'),
                                          fit: BoxFit.cover)),
                                  height: 300,
                                  width: 200,
                                  child: Column(
                                    mainAxisAlignment: MainAxisAlignment.end,
                                    children: [
                                      Text(
                                        change.cities[index],
                                        style: GoogleFonts.lato(
                                            color: Colors.white,
                                            fontSize: 32,
                                            fontWeight: FontWeight.w900),
                                      ),
                                      SizedBox(
                                        height: 10,
                                      )
                                    ],
                                  ),
                                ),
                              ),
                            ),
                          );
                        }),
                  ),
                ],
              ),
          ),
        ],
      ),
    );
  }
}
