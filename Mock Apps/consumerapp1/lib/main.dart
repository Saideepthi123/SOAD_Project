import 'dart:convert';

import 'package:consumerapp1/HomeScreen.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'globals.dart';

import 'package:http/http.dart';
import 'ServerCalls.dart';
void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: FutureBuilder(
            future: DataService.getToken(),
            builder: (context, snapshot){
              if(snapshot.connectionState==ConnectionState.done){
                if(snapshot.hasData){
                  Response response=snapshot.data;
                  print(response.body);
                  if(response.statusCode==200){
                    set_APIKey(jsonDecode(response.body));
                    return HomeScreen();
                  }
                }
                if(snapshot.hasError){
                  return Text("Error!");
                }
              }
              return Center(child: CircularProgressIndicator());
            },
        ),
      ),
    );
  }
}
