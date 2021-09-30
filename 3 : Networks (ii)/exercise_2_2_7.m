r =         [0 0 0 1 0 1 0 1 0; 
             0 0 0 0 0 0 1 0 0; 
             0 0 0 0 1 1 0 0 0; 
             0 0 1 0 0 0 0 0 0; 
             1 0 0 0 0 0 0 0 0; 
             0 1 0 0 0 0 0 0 0; 
             1 0 0 0 0 0 0 0 0;
             1 0 0 0 0 0 0 0 0;
             1 0 0 0 0 0 0 1 0];
         
         
         
gr = biograph(r,{'F6P' 'F16BP' 'F26BP' 'E1' 'E2' 'E3' 'E4' 'E5' 'G6P'});
gr.LayoutType = 'equilibrium'
dolayout(gr)
set(gr.Nodes(1:3),'Shape','ellipse')
set(gr.Nodes(9),'Shape','ellipse')
set(gr.Nodes,'FontSize',10)
set(gr.Nodes(4:end),'Color',[0.5,0.8,1])
set(gr.Nodes(1:3),'Color',[0.2,0.8,0.1])
set(gr.Nodes(9),'Color',[0.2,0.8,0.1])
view(gr)

