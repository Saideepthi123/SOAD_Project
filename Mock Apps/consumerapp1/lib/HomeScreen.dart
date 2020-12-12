import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:google_fonts/google_fonts.dart';

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final cities = ['Ahmedabad', 'Vizag', 'Vadodara', 'Delhi'];

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
              alignment: Alignment.center,
              height: _screensize.height * 0.56,
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.vertical(top: Radius.circular(30)),
              ),
              child: SizedBox(
                height: 150,
                width: 150,
                child: ListView.builder(
                  scrollDirection: Axis.horizontal,
                  itemCount: cities.length,
                  itemBuilder: (context, count) {
                    return SizedBox(
                      child: Card(
                        color: Colors.blueAccent,
                        child: Container(
                          alignment: Alignment.center,
                          child: Column(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Container(
                                decoration: BoxDecoration(
                                    image: DecorationImage(
                                        image:
                                            AssetImage("assets/City1.jpg"))),
                              ),
                              Text(cities[count]),
                            ],
                          ),
                        ),
                      ),
                    );
                  },
                ),
              ),
            ),
          ],
        )
      ],
    ));
  }
}
