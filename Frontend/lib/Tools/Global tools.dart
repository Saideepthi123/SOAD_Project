import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:travel/Screens/City.dart';
import '../Screens/HomePage.dart';

class TopAppBar extends AppBar {
  BuildContext context;

  @override
  // TODO: implement leading
  Widget get leading => IconButton(
        icon: Icon(FontAwesomeIcons.plane),
        onPressed: () {
          Navigator.push(
              context, MaterialPageRoute(builder: (context) => HomePage()));
        },
      );

  @override
  Widget get title => InkWell(
      onTap: () {
        Navigator.push(
            context, MaterialPageRoute(builder: (context) => CityPage()));
      },
      child: Text("Hello"));

  TopAppBar(this.context);
}
