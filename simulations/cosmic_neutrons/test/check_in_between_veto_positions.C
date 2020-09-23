void check_in_between_veto_positions(string filename="babyIAXO_Between_Cadmium2mm_Depth5mm_neutron_N1E3_run1.root"){

    cout << filename << endl;
    int number_of_entries = run0->GetEntries();
    int number_of_primaries = md0_restG4Simulationrun->GetNumberOfEvents();
    cout << "Number of entries: " << number_of_entries << " / " << number_of_primaries << " (" << float(number_of_entries)/number_of_primaries*100 << "%)" << endl;

    cout << endl;

    cout << "Generator type: " << md0_restG4Simulationrun->GetGeneratorType() << endl;
    TVector3 generator_position = md0_restG4Simulationrun->GetGeneratorPosition();
    cout << "Generator position: (" << generator_position.X() << ", " << generator_position.Y() << ", " << generator_position.Z() << ")" << endl;

    cout << endl;

    std::vector<int> volumes_of_interest;

    cout << "Active volumes:" << endl;
    for (int i = 0; i < md0_restG4Simulationrun->GetNumberOfActiveVolumes(); i++){
        string volume_name = (string)md0_restG4Simulationrun->GetActiveVolumeName(i);
        cout << i << " : " << volume_name << endl;
        if (volume_name.find("scintillatorSheet") != std::string::npos){
            volumes_of_interest.push_back(i);
        }
    }

    cout << endl;

    cout << "scintillatorSheet volumes:" << endl;
    for (auto & i : volumes_of_interest){
        cout << i << " : " << md0_restG4Simulationrun->GetActiveVolumeName(i) << endl;
    }

    cout << endl;

    TGeoNode *node = gGeoManager->GetTopNode();
    // node->GetNodes()->Print();
    for (int k = 0; k < node->GetNodes()->GetSize(); k++){
        string volume_name = (string)node->GetVolume()->GetNode(k)->GetName();

        for (auto & i : volumes_of_interest){
            if (volume_name == (string)md0_restG4Simulationrun->GetActiveVolumeName(i)){

                auto matrix = node->GetVolume()->GetNode(k)->GetMatrix();
                double y = matrix->GetTranslation()[1];

                cout << "Node " << k << " : " << (string)node->GetVolume()->GetNode(k)->GetName() << "\t" << " y = " << y << endl;

                break;
            }
        }
    }
}