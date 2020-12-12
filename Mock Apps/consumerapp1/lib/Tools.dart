import 'package:flutter/material.dart';

class SearchBar extends StatelessWidget {
  List<String> suggestions;
  double width;
  Function onChange;
  SearchBar({this.suggestions,this.width,this.onChange});
  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 10,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(50),
      ),
      child: Container(
        padding: EdgeInsets.all(8),
        height: 50,
        child: Row(
          children: [
            Icon(Icons.search),
            SizedBox(width: 8,),
            Container(
              width: width*0.8,
              padding: EdgeInsets.only(bottom: 10),
              child: TextField(
                autofillHints: suggestions,
                enableSuggestions: true,
                decoration: InputDecoration(
                  border: InputBorder.none,
                ),
                onTap: () {},
                // onEditingComplete: onChange,
                onChanged: onChange,
              ),
            )
          ],
        ),
      ),
    );
  }
}