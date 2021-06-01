figure ()
points = 0:0.01*pi:12*pi;
plot( 0, 0, 'w');
axis([-25 50 -25 25]);
hold on;
R = 1;
k = 5;
l = 2;
for i = 1:length(points)
    t = points(i);
%     x = 13*cos(t) - 5*cos(11*t/5);
%     y = 13*sin(t) + 3*sin(11*t/5);
    x = (1-k)*cos(t) + (l*k)*cos((1-k/k))*t;
    y = (1-k)*sin(t) + (l*k)*sin((1-k/k))*t;
    plot( x, y,'b--o' );
    pause(0.01);
end
