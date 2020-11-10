import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:travel/APIcalls/Auth.dart';
import 'package:travel/Screens/City.dart';
import 'package:travel/Screens/loginSign.dart';
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

  @override
  List<Widget> get actions => [
        RaisedButton(
          child: Text("Logout"),
          onPressed: () {
            AuthService.logout().then((value) {
              print(value.body);
                  Navigator.pushAndRemoveUntil(
                      context,
                      MaterialPageRoute(builder: (context) => LogIn()),
                      (route) => false);
                });
          },
        )
      ];
  TopAppBar(this.context);
}
