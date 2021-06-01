     %1 2 3 4 5 6 7 8 9 0 1 2
fw = [0 1 0 0 1 0 1 0 0 0 0 0; %1Plant res
      0 0 1 1 0 0 0 0 0 0 0 0; %2bact
      0 0 0 0 0 0 0 0 0 0 0 0; %3bact prot
      0 0 0 0 0 0 0 0 1 0 0 0; %4bact nema
      0 0 0 0 0 1 0 0 1 0 0 0; %5fungi
      0 0 0 0 0 0 0 0 1 0 0 0; %6fungi nema
      0 0 0 0 0 0 0 1 0 0 0 0; %7myco
      0 0 0 0 0 1 0 0 0 0 0 0; %8fungi pro
      0 0 0 0 0 0 0 0 0 1 1 1; %9micro
      0 0 0 0 0 0 0 0 0 0 0 0; %0enchy
      0 0 0 0 0 0 0 0 0 0 0 0; %1macro
      0 0 0 0 0 0 0 0 0 0 0 0; %2earth
     
     ];
nodes = {'Plant Residues'
         'Bacteria'
         'Bacteria-feeding Protozoa'
         'Bacteria-Feeding Nematodes'
         'Fungi' 
         'Fungal-feeding Nematodes'
         'Mycorrhizae'
         'Fungal-feeding Protozoa'
         'Microarthropods (Collembola, Mites)'
         'Enchytraeids'
         'Macroarthropods'
         'Earthworms'
         };
     
g = biograph(fw,nodes);
% g.LayoutType = '';
dolayout(g);
vg = view(g);

set(vg.nodes(1),'Shape','Circle');

set(vg.nodes(2),'Color',[0.9290, 0.6940, 0.1250]);
set(vg.nodes(3),'Color',[0.9290, 0.6940, 0.1250]);
set(vg.nodes(4),'Color',[0.9290, 0.6940, 0.1250]);

set(vg.nodes(5),'Color',[0 1 1]);
set(vg.nodes(6),'Color',[0 1 1]);
set(vg.nodes(7),'Color',[0 1 1]);
set(vg.nodes(8),'Color',[0 1 1]);
set(vg.nodes(9),'Color',[0 1 1]);
set(vg.nodes(10),'Color',[0 1 1]);
set(vg.nodes(11),'Color',[0 1 1]);
set(vg.nodes(12),'Color',[0 1 1]);
