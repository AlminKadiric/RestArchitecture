{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "title": "Album",
  "description": "An album from a home collection",
  "type": "object",
    
  "properties": {
    
     "id": {
        "description": "The unique identifier for an album",
        "type": "integer"
     },
        
     "name": {
        "description": "Name of the album",
        "type": "string"
     },
    
     "year": {
        "description": "Year of release",
        "type": "number"
     },
 
     "author": {
        "description": "Name of the author",
        "type": "string"
     }
  },
    
  "required": ["id", "name", "year", "author"]
}