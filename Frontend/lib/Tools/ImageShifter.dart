import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:travel/Models/Image.dart';

class ImageShifter extends StatefulWidget {
  @override
  _ImageShifterState createState() => _ImageShifterState();
}

class _ImageShifterState extends State<ImageShifter> {
  @override
  Widget build(BuildContext context) {
    var change = Provider.of<BackImage>(context);
    final myTween = Tween<Offset>(
      begin: const Offset(-1.0, 0.0),
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
