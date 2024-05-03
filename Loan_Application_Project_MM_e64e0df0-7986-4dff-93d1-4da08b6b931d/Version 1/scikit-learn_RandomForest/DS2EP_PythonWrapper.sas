data sasep.out;
   dcl package pymas pm;
   dcl package logger logr('App.MM.Python.DS2');
   dcl varchar(32767) character set utf8 pypgm;
   dcl double resultCode revision;
   dcl double "DEFAULT";
   dcl double "LOANREQUEST";
   dcl double "HOMEVALUE";
   dcl double "YEARSONJOB";
   dcl double "DEROGATORYMARKS";
   dcl double "DELINQUENCIES";
   dcl double "CREDLINEAGE";
   dcl double "INQUIRIES";
   dcl double "CREDLINES";
   dcl double "DEBTINCRATIO";
   dcl double "INCOME";
   dcl double "LOANTOVALUE";
   dcl double "P_DEFAULT0";
   dcl double "P_DEFAULT1";
   dcl varchar(100) "I_DEFAULT";

   method score(
   double "DELINQUENCIES",
   double "DEROGATORYMARKS",
   double "INQUIRIES",
   double "CREDLINEAGE",
   double "CREDLINES",
   double "DEBTINCRATIO",
   double "LOANREQUEST",
   double "HOMEVALUE",
   double "INCOME",
   double "LOANTOVALUE",
   double "YEARSONJOB",
   in_out double resultCode,
   in_out double "P_DEFAULT0",
   in_out double "P_DEFAULT1",
   in_out varchar(100) "I_DEFAULT");

      resultCode = revision = 0;
      if null(pm) then do;
         pm = _new_ pymas();
         resultCode = pm.useModule('model_exec_1389f4c4-27ec-4235-80c3-fac1e307d5a5', 1);
         if resultCode then do;
            resultCode = pm.appendSrcLine('import sys');
            resultCode = pm.appendSrcLine('sys.path.append("/models/resources/viya/bb6ea2d6-c061-416a-a872-0de47f74c66d/")');
            resultCode = pm.appendSrcLine('import settings_bb6ea2d6_c061_416a_a872_0de47f74c66d');
            resultCode = pm.appendSrcLine('settings_bb6ea2d6_c061_416a_a872_0de47f74c66d.pickle_path = "/models/resources/viya/bb6ea2d6-c061-416a-a872-0de47f74c66d/"');
            resultCode = pm.appendSrcLine('import score_rf2');
            resultCode = pm.appendSrcLine('def score_method(DELINQUENCIES, DEROGATORYMARKS, INQUIRIES, CREDLINEAGE, CREDLINES, DEBTINCRATIO, LOANREQUEST, HOMEVALUE, INCOME, LOANTOVALUE, YEARSONJOB):');
            resultCode = pm.appendSrcLine('    "Output: P_DEFAULT0, P_DEFAULT1, I_DEFAULT"');
            resultCode = pm.appendSrcLine('    return score_rf2.score_method(DELINQUENCIES, DEROGATORYMARKS, INQUIRIES, CREDLINEAGE, CREDLINES, DEBTINCRATIO, LOANREQUEST, HOMEVALUE, INCOME, LOANTOVALUE, YEARSONJOB)');

            revision = pm.publish(pm.getSource(), 'model_exec_1389f4c4-27ec-4235-80c3-fac1e307d5a5');
            if ( revision < 1 ) then do;
               logr.log( 'e', 'py.publish() failed.');
               resultCode = -1;
               return;
            end;
         end;
      end;

      resultCode = pm.useMethod('score_method');
      if resultCode then do;
         logr.log('E', 'useMethod() failed. resultCode=$s', resultCode);
         return;
      end;
      resultCode = pm.setDouble('DELINQUENCIES', DELINQUENCIES);
      if resultCode then
         logr.log('E', 'setDouble for DELINQUENCIES failed.  resultCode=$s', resultCode);
      resultCode = pm.setDouble('DEROGATORYMARKS', DEROGATORYMARKS);
      if resultCode then
         logr.log('E', 'setDouble for DEROGATORYMARKS failed.  resultCode=$s', resultCode);
      resultCode = pm.setDouble('INQUIRIES', INQUIRIES);
      if resultCode then
         logr.log('E', 'setDouble for INQUIRIES failed.  resultCode=$s', resultCode);
      resultCode = pm.setDouble('CREDLINEAGE', CREDLINEAGE);
      if resultCode then
         logr.log('E', 'setDouble for CREDLINEAGE failed.  resultCode=$s', resultCode);
      resultCode = pm.setDouble('CREDLINES', CREDLINES);
      if resultCode then
         logr.log('E', 'setDouble for CREDLINES failed.  resultCode=$s', resultCode);
      resultCode = pm.setDouble('DEBTINCRATIO', DEBTINCRATIO);
      if resultCode then
         logr.log('E', 'setDouble for DEBTINCRATIO failed.  resultCode=$s', resultCode);
      resultCode = pm.setDouble('LOANREQUEST', LOANREQUEST);
      if resultCode then
         logr.log('E', 'setDouble for LOANREQUEST failed.  resultCode=$s', resultCode);
      resultCode = pm.setDouble('HOMEVALUE', HOMEVALUE);
      if resultCode then
         logr.log('E', 'setDouble for HOMEVALUE failed.  resultCode=$s', resultCode);
      resultCode = pm.setDouble('INCOME', INCOME);
      if resultCode then
         logr.log('E', 'setDouble for INCOME failed.  resultCode=$s', resultCode);
      resultCode = pm.setDouble('LOANTOVALUE', LOANTOVALUE);
      if resultCode then
         logr.log('E', 'setDouble for LOANTOVALUE failed.  resultCode=$s', resultCode);
      resultCode = pm.setDouble('YEARSONJOB', YEARSONJOB);
      if resultCode then
         logr.log('E', 'setDouble for YEARSONJOB failed.  resultCode=$s', resultCode);
      resultCode = pm.execute();
      if (resultCode) then
         logr.log('E', 'Error: pm.execute failed.  resultCode=$s', resultCode);
      else do;
         "P_DEFAULT0" = pm.getDouble('P_DEFAULT0');
         "P_DEFAULT1" = pm.getDouble('P_DEFAULT1');
         "I_DEFAULT" = pm.getString('I_DEFAULT');
      end;
   end;

   method run();
      set SASEP.IN;
      score("DELINQUENCIES","DEROGATORYMARKS","INQUIRIES","CREDLINEAGE","CREDLINES","DEBTINCRATIO","LOANREQUEST","HOMEVALUE","INCOME","LOANTOVALUE","YEARSONJOB", resultCode, "P_DEFAULT0", "P_DEFAULT1", "I_DEFAULT");
   end;
enddata;
