package pythonScore / overwrite=yes;
dcl package pymas pm;
dcl package logger logr('App.tk.MAS');
dcl varchar(32767) character set utf8 pypgm;
dcl int resultCode revision;

method score(double "CredLineAge",
double "CredLines",
double "DebtIncRatio",
double "Delinquencies",
double "DerogatoryMarks",
double "HomeValue",
double "Income",
double "Inquiries",
varchar(100) "JobType",
double "LoanRequest",
double "LoanToValue",
double "YearsOnJob",
in_out double resultCode,
in_out varchar(100) "I_Default",
in_out double "P_Default0",
in_out double "P_Default1");

   resultCode = revision = 0;
   if null(pm) then do;
      pm = _new_ pymas();
      resultCode = pm.useModule('model_exec_cee226c6-57ba-4c2c-823b-b48bfb5e12cb', 1);
      if resultCode then do;
         resultCode = pm.appendSrcLine('import sys');
         resultCode = pm.appendSrcLine('sys.path.append("/models/resources/viya/18a81ad7-db11-4470-8a0b-fc3d807efce2/")');
         resultCode = pm.appendSrcLine('import settings_18a81ad7_db11_4470_8a0b_fc3d807efce2');
         resultCode = pm.appendSrcLine('settings_18a81ad7_db11_4470_8a0b_fc3d807efce2.pickle_path = "/models/resources/viya/18a81ad7-db11-4470-8a0b-fc3d807efce2/"');
         resultCode = pm.appendSrcLine('import _dj5n7wg1ne74bjo4ln9lur5fz_85319305_591b_4548_a52e_8fbeafcf4e20');
         resultCode = pm.appendSrcLine('def score_method(Delinquencies, DerogatoryMarks, Inquiries, JobType, CredLineAge, CredLines, DebtIncRatio, LoanRequest, HomeValue, Income, LoanToValue, YearsOnJob):');
         resultCode = pm.appendSrcLine('    "Output: P_Default0, P_Default1, I_Default"');
         resultCode = pm.appendSrcLine('    return _dj5n7wg1ne74bjo4ln9lur5fz_85319305_591b_4548_a52e_8fbeafcf4e20.score_method(Delinquencies, DerogatoryMarks, Inquiries, JobType, CredLineAge, CredLines, DebtIncRatio, LoanRequest, HomeValue, Income, LoanToValue, YearsOnJob)');

         revision = pm.publish(pm.getSource(), 'model_exec_cee226c6-57ba-4c2c-823b-b48bfb5e12cb');
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
   resultCode = pm.setDouble('Delinquencies', "Delinquencies");
   if resultCode then
      logr.log('E', 'setDouble for Delinquencies failed.  resultCode=$s', resultCode);
   resultCode = pm.setDouble('DerogatoryMarks', "DerogatoryMarks");
   if resultCode then
      logr.log('E', 'setDouble for DerogatoryMarks failed.  resultCode=$s', resultCode);
   resultCode = pm.setDouble('Inquiries', "Inquiries");
   if resultCode then
      logr.log('E', 'setDouble for Inquiries failed.  resultCode=$s', resultCode);
   resultCode = pm.setString('JobType', "JobType");
   if resultCode then
      logr.log('E', 'setString for JobType failed.  resultCode=$s', resultCode);
   resultCode = pm.setDouble('CredLineAge', "CredLineAge");
   if resultCode then
      logr.log('E', 'setDouble for CredLineAge failed.  resultCode=$s', resultCode);
   resultCode = pm.setDouble('CredLines', "CredLines");
   if resultCode then
      logr.log('E', 'setDouble for CredLines failed.  resultCode=$s', resultCode);
   resultCode = pm.setDouble('DebtIncRatio', "DebtIncRatio");
   if resultCode then
      logr.log('E', 'setDouble for DebtIncRatio failed.  resultCode=$s', resultCode);
   resultCode = pm.setDouble('LoanRequest', "LoanRequest");
   if resultCode then
      logr.log('E', 'setDouble for LoanRequest failed.  resultCode=$s', resultCode);
   resultCode = pm.setDouble('HomeValue', "HomeValue");
   if resultCode then
      logr.log('E', 'setDouble for HomeValue failed.  resultCode=$s', resultCode);
   resultCode = pm.setDouble('Income', "Income");
   if resultCode then
      logr.log('E', 'setDouble for Income failed.  resultCode=$s', resultCode);
   resultCode = pm.setDouble('LoanToValue', "LoanToValue");
   if resultCode then
      logr.log('E', 'setDouble for LoanToValue failed.  resultCode=$s', resultCode);
   resultCode = pm.setDouble('YearsOnJob', "YearsOnJob");
   if resultCode then
      logr.log('E', 'setDouble for YearsOnJob failed.  resultCode=$s', resultCode);
   resultCode = pm.execute();
   if (resultCode) then
      logr.log('E', 'Error: pm.execute failed.  resultCode=$s', resultCode);
   else do;
      "P_Default0" = pm.getDouble('P_Default0');
      "P_Default1" = pm.getDouble('P_Default1');
      "I_Default" = pm.getString('I_Default');
   end;
end;

endpackage;
