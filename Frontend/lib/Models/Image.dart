import 'package:flutter/material.dart';

class BackImage with ChangeNotifier{
  Widget _currentimage;
  List _cities = ["Delhi", "Vadodara", "Vizag","SriCity","Mumbai"];
  String _currname;
  String _metadata;

  Widget get currentimage => _currentimage;
  List get cities => _cities; 
  String get cityname => _currname;
  String get metadata => _metadata;

  currimage(String image){
    _currentimage = Container(
      key: Key(image),
      decoration: BoxDecoration(
        image: DecorationImage(image: AssetImage('img/Image'+image+".jpg"),fit: BoxFit.fill )
      ),
    );
    notifyListeners();
  }

  set cityname(String inp){
    _currname = inp;
    notifyListeners();
  }
  set metadata(String inp){
    _metadata = inp;
    notifyListeners();
  }
  BackImage(this._currentimage,this._currname,this._metadata);
}