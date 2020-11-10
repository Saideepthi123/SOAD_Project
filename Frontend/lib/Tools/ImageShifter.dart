import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:travel/Models/Image.dart';


class ImageShifter extends StatelessWidget {
  double xOffset;
  double yOffset;
  ImageShifter({this.xOffset,this.yOffset});
  @override
  Widget build(BuildContext context) {
    var change = Provider.of<BackImage>(context);
    final myTween = Tween<Offset>(
      begin: new Offset(xOffset, yOffset),
      end: Offset.zero,
    );
    return Container(
      child: AnimatedSwitcher(
        transitionBuilder: (Widget child, Animation<double> animation) =>
            SlideTransition(
              position: animation.drive(myTween),
              child: child,
            ),
        duration: Duration(milliseconds: 700),
        child: change.currentimage,
      ),
    );
  }
}

