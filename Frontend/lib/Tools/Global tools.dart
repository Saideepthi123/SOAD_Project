import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
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
  TopAppBar(this.context);
}
