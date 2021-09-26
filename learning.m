ther=createpde('thermal','steadystate');
importGeometry(ther,'hub_final.STL');
pdegplot(ther,'FaceAlpha',0.5);
generateMesh(ther,'Hmax',0.09);
ther.Mesh;
pdemesh(ther);
