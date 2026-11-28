# Final connection readback recovery

After delivery commit 9920a04ab40ce2970e10492fe8558421654657da, connector successfully read report/receipt/audit, but BATCH_STATE fetch returned Transport closed. Retried main ref via connector: same9920a04a. Fixed-commit raw BATCH_STATE fullGET4070469bytes parsed successfully: onlyPARTIAL1330Z3/6,next4,leaseNone,receiptpathcorrect. Transient read transport recovered, not an upload/commit failure. Prior41file/fullhash16PNG receipt remains valid. No additional production cycle credited.
