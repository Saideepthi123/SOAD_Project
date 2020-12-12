import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:consumerapp1/City.dart';

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final cities = ['Vizag','Mumbai', 'Vadodara', 'Delhi'];

  @override
  Widget build(BuildContext context) {
    final _screensize = MediaQuery.of(context).size;
    return Container(
        child: Stack(
      children: [
        Container(
          height: _screensize.height * 0.56,
          decoration: BoxDecoration(
              image: DecorationImage(
                  image: AssetImage('assets/City.jpg'), fit: BoxFit.fill)),
        ),
        Container(
          margin: EdgeInsets.only(top: 15),
          alignment: Alignment.topCenter,
          child: Text(
            "Travel",
            style: GoogleFonts.lato(
                fontSize: 48, color: Colors.white, fontWeight: FontWeight.w900),
          ),
        ),
        Column(
          mainAxisAlignment: MainAxisAlignment.end,
          children: [
            Container(
              padding: EdgeInsets.all(20),
              alignment: Alignment.center,
              height: _screensize.height * 0.56,
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.vertical(top: Radius.circular(30)),
              ),
              child: SizedBox(
                // height: _screensize.height*0.5,
                // width: _screensize.height*0.5,
                child: Center(
                  child: ListView(
                    // itemExtent: 200,
                    // diameterRatio: 1.5,
                    children: [
                      ...cities.map((String name) {
                        return Padding(
                          padding: const EdgeInsets.all(8.0),
                          child: InkWell(
                            onTap: (){
                              print("tapped");
                              Navigator.push(context,MaterialPageRoute(builder: (context) => CityPage(cityIdx: 1)));
                            },
                            child: Container(
                              height: _screensize.height*0.4,
                              width: _screensize.width*0.5,
                              decoration: BoxDecoration(
                                  // color: CupertinoColors.white,
                                  borderRadius: BorderRadius.circular(10),
                                  border: Border.all(
                                      width: 1, color: CupertinoColors.inactiveGray),
                                  image: DecorationImage(
                                      image: AssetImage('assets/CardImage'+ name + '.jpg'), fit: BoxFit.fill)
                              ),
                              padding: EdgeInsets.all(10),
                              child: Center(
                                child: Text(name,style: GoogleFonts.lato(
                                    fontSize: 37,color: Colors.white, fontWeight: FontWeight.bold
                                )
                                ),
                              ),
                            ),
                          ),
                        );
                      })
                    ],
                  ),
                ),
              ),
            ),
          ],
        )
      ],
    ));
  }
}
