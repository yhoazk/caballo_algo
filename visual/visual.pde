void setup() {
  size(500, 500);
  background(204);
 // outerRad = min(width, height) * 0.4;
 // innerRad = outerRad * 0.6;
   noLoop();  // Draw only one time
}
  int size = 40;
  int step = 0;
void drawMov(int x0, int y0, int x1, int y1){
  
  line(size*(x0 + 1.5), size*(y0 + 1.5), size*(x1 + 1.5), size*(y1 + 1.5));
}

void drawPoint(int x0, int y0, char c){
//  void drawPoint(int x0, int y0){
  
  if(c == 'X')
  {
    fill(127);
  }
  else if(c == 'R')
  {
    fill(250,0,0);
    
  }
  else 
  {
    fill(0,250,0);
  }
  ellipse(size*(x0 + 1.5), size*(y0 + 1.5), size/2, size/2);
  fill(0);
  text(step++, size*(x0 + 1.3), size*(y0 + 1.6));
  
}


void drawPoint_small(int x0, int y0, char c){
//  void drawPoint(int x0, int y0){
  
  if(c == 'X')
  {
    fill(127);
  }
  else if(c == 'R')
  {
    fill(250,0,0);
    
  }
  else 
  {
    fill(0,250,0);
  }
  ellipse(size*(x0 + 1.5), size*(y0 + 1.5), size/4, size/4);
  fill(0);
  text(step++, size*(x0 + 1.3), size*(y0 + 1.6));
  
}

int [][] points = {{1,2},{2,3},{3,4}};
int [][] positions = new int[8][8];
void draw() {

  int i = size;
  int j = size;
  int x = 0;
  int y = 0;
  int c = 0;
  background(204);

  for(;y<8;y=y+1)
  {
     
    for(x=0;x<8;x=x+1)
    {
      /*
      if(x%2 == 1 &&  y%2 == 1)
      {
        fill(10, 102, 0);
      }
      else
      {
        fill(204, 102, 0);
      }*/
      beginShape();
        vertex(i, j);
        vertex(i + size, j);
        vertex(i + size, j + size);
        vertex(i, j + size);
      endShape(CLOSE);
      i = i + size;
      fill(204, 102, 200);
      text(c++, i,j);
      fill(204, 102, 0);
      //positions[x][y] = 
     
     // ellipse(x*size+1.5*size,y*size+1.5*size,size/2,size/2);
    }
    j = j + size;
    i = size;
  }
   //line(size*(x + 1.5), size*(y + 1.5), size*(x + 2.5),size*(y + 2.5));

//  drawMov(1,1,5,5);

//caballo
/////////////////////

drawPoint( 0 , 5 ,'X' );
drawPoint( 7 , 5 ,'X' );
drawPoint( 3 , 6 ,'X' );
drawPoint( 4 , 7 ,'X' );
drawPoint( 5 , 5 ,'X' );
drawPoint( 2 , 7 ,'X' );
drawPoint( 2 , 0 ,'X' );
drawPoint( 4 , 3 ,'X' );
drawPoint( 3 , 7 ,'X' );
drawPoint( 6 , 4 ,'X' );
drawPoint( 7 , 6 ,'X' );
drawPoint( 7 , 0 ,'X' );
drawPoint( 2 , 3 ,'X' );
drawPoint( 7 , 1 ,'X' );
drawPoint( 0 , 4 ,'X' );
drawPoint( 2 , 4 ,'X' );
////////////__
drawPoint( 5 , 6 ,'X' );
drawMov( 5 , 6 , 3 , 5 );
drawPoint_small( 2 , 7 ,'G' );
drawPoint_small( 4 , 7 ,'G' );
drawPoint_small( 5 , 6 ,'G' );
drawPoint_small( 5 , 4 ,'G' );
drawPoint_small( 4 , 3 ,'G' );
drawPoint_small( 2 , 3 ,'G' );
drawPoint_small( 1 , 4 ,'G' );
drawPoint_small( 1 , 6 ,'G' );



drawPoint_small( 3 , 5 ,'R' );

}
