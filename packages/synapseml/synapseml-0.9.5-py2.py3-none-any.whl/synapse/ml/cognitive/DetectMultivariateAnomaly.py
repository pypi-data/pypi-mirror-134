# Copyright (C) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in project root for information.


import sys
if sys.version >= '3':
    basestring = str

from pyspark import SparkContext, SQLContext
from pyspark.sql import DataFrame
from pyspark.ml.param.shared import *
from pyspark import keyword_only
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from synapse.ml.core.serialize.java_params_patch import *
from pyspark.ml.wrapper import JavaTransformer, JavaEstimator, JavaModel
from pyspark.ml.evaluation import JavaEvaluator
from pyspark.ml.common import inherit_doc
from synapse.ml.core.schema.Utils import *
from pyspark.ml.param import TypeConverters
from synapse.ml.core.schema.TypeConversionUtils import generateTypeConverter, complexTypeConverter


@inherit_doc
class DetectMultivariateAnomaly(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        backoffs (list): array of backoffs to use in the handler
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        connectionString (object): Connection String for your storage account used for uploading files.
        containerName (object): Container that will be used to upload files to.
        endTime (object): A required field, end time of data to be used for detection/generating multivariate anomaly detection model, should be date-time.
        endpoint (object): End Point for your storage account used for uploading files.
        errorCol (object): column to hold http errors
        initialPollingDelay (int): number of milliseconds to wait before first poll for result
        inputCols (list): The names of the input columns
        intermediateSaveDir (object): Directory name of which you want to save the intermediate data produced while training.
        maxPollingRetries (int): number of times to poll
        modelId (object): Format - uuid. Model identifier.
        outputCol (object): The name of the output column
        pollingDelay (int): number of milliseconds to wait between polling
        sasToken (object): SAS Token for your storage account used for uploading files.
        startTime (object): A required field, start time of data to be used for detection/generating multivariate anomaly detection model, should be date-time.
        storageKey (object): Storage Key for your storage account used for uploading files.
        storageName (object): Storage Name for your storage account used for uploading files.
        subscriptionKey (object): the API key to use
        suppressMaxRetriesExceededException (bool): set true to suppress the maxumimum retries exception and report in the error column
        timeout (float): number of seconds to wait before closing the connection
        timestampCol (object): Timestamp column name
        url (object): Url of the service
    """

    backoffs = Param(Params._dummy(), "backoffs", "array of backoffs to use in the handler", typeConverter=TypeConverters.toListInt)
    
    concurrency = Param(Params._dummy(), "concurrency", "max number of concurrent calls", typeConverter=TypeConverters.toInt)
    
    concurrentTimeout = Param(Params._dummy(), "concurrentTimeout", "max number seconds to wait on futures if concurrency >= 1", typeConverter=TypeConverters.toFloat)
    
    connectionString = Param(Params._dummy(), "connectionString", "Connection String for your storage account used for uploading files.")
    
    containerName = Param(Params._dummy(), "containerName", "Container that will be used to upload files to.")
    
    endTime = Param(Params._dummy(), "endTime", "A required field, end time of data to be used for detection/generating multivariate anomaly detection model, should be date-time.")
    
    endpoint = Param(Params._dummy(), "endpoint", "End Point for your storage account used for uploading files.")
    
    errorCol = Param(Params._dummy(), "errorCol", "column to hold http errors")
    
    initialPollingDelay = Param(Params._dummy(), "initialPollingDelay", "number of milliseconds to wait before first poll for result", typeConverter=TypeConverters.toInt)
    
    inputCols = Param(Params._dummy(), "inputCols", "The names of the input columns", typeConverter=TypeConverters.toListString)
    
    intermediateSaveDir = Param(Params._dummy(), "intermediateSaveDir", "Directory name of which you want to save the intermediate data produced while training.")
    
    maxPollingRetries = Param(Params._dummy(), "maxPollingRetries", "number of times to poll", typeConverter=TypeConverters.toInt)
    
    modelId = Param(Params._dummy(), "modelId", "Format - uuid. Model identifier.")
    
    outputCol = Param(Params._dummy(), "outputCol", "The name of the output column")
    
    pollingDelay = Param(Params._dummy(), "pollingDelay", "number of milliseconds to wait between polling", typeConverter=TypeConverters.toInt)
    
    sasToken = Param(Params._dummy(), "sasToken", "SAS Token for your storage account used for uploading files.")
    
    startTime = Param(Params._dummy(), "startTime", "A required field, start time of data to be used for detection/generating multivariate anomaly detection model, should be date-time.")
    
    storageKey = Param(Params._dummy(), "storageKey", "Storage Key for your storage account used for uploading files.")
    
    storageName = Param(Params._dummy(), "storageName", "Storage Name for your storage account used for uploading files.")
    
    subscriptionKey = Param(Params._dummy(), "subscriptionKey", "the API key to use")
    
    suppressMaxRetriesExceededException = Param(Params._dummy(), "suppressMaxRetriesExceededException", "set true to suppress the maxumimum retries exception and report in the error column", typeConverter=TypeConverters.toBoolean)
    
    timeout = Param(Params._dummy(), "timeout", "number of seconds to wait before closing the connection", typeConverter=TypeConverters.toFloat)
    
    timestampCol = Param(Params._dummy(), "timestampCol", "Timestamp column name")
    
    url = Param(Params._dummy(), "url", "Url of the service")

    
    @keyword_only
    def __init__(
        self,
        java_obj=None,
        backoffs=[100,500,1000],
        concurrency=1,
        concurrentTimeout=None,
        connectionString=None,
        containerName=None,
        endTime=None,
        endpoint=None,
        errorCol="DetectMultivariateAnomaly_76ec62354b0d_error",
        initialPollingDelay=300,
        inputCols=None,
        intermediateSaveDir=None,
        maxPollingRetries=1000,
        modelId=None,
        outputCol="DetectMultivariateAnomaly_76ec62354b0d_output",
        pollingDelay=300,
        sasToken=None,
        startTime=None,
        storageKey=None,
        storageName=None,
        subscriptionKey=None,
        subscriptionKeyCol=None,
        suppressMaxRetriesExceededException=False,
        timeout=60.0,
        timestampCol="timestamp",
        url=None
        ):
        super(DetectMultivariateAnomaly, self).__init__()
        if java_obj is None:
            self._java_obj = self._new_java_obj("com.microsoft.azure.synapse.ml.cognitive.DetectMultivariateAnomaly", self.uid)
        else:
            self._java_obj = java_obj
        self._setDefault(backoffs=[100,500,1000])
        self._setDefault(concurrency=1)
        self._setDefault(errorCol="DetectMultivariateAnomaly_76ec62354b0d_error")
        self._setDefault(initialPollingDelay=300)
        self._setDefault(maxPollingRetries=1000)
        self._setDefault(outputCol="DetectMultivariateAnomaly_76ec62354b0d_output")
        self._setDefault(pollingDelay=300)
        self._setDefault(suppressMaxRetriesExceededException=False)
        self._setDefault(timeout=60.0)
        self._setDefault(timestampCol="timestamp")
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
    
        if java_obj is None:
            for k,v in kwargs.items():
                if v is not None:
                    getattr(self, "set" + k[0].upper() + k[1:])(v)

    @keyword_only
    def setParams(
        self,
        backoffs=[100,500,1000],
        concurrency=1,
        concurrentTimeout=None,
        connectionString=None,
        containerName=None,
        endTime=None,
        endpoint=None,
        errorCol="DetectMultivariateAnomaly_76ec62354b0d_error",
        initialPollingDelay=300,
        inputCols=None,
        intermediateSaveDir=None,
        maxPollingRetries=1000,
        modelId=None,
        outputCol="DetectMultivariateAnomaly_76ec62354b0d_output",
        pollingDelay=300,
        sasToken=None,
        startTime=None,
        storageKey=None,
        storageName=None,
        subscriptionKey=None,
        subscriptionKeyCol=None,
        suppressMaxRetriesExceededException=False,
        timeout=60.0,
        timestampCol="timestamp",
        url=None
        ):
        """
        Set the (keyword only) parameters
        """
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        return self._set(**kwargs)

    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
        return JavaMMLReader(cls)

    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
        return "com.microsoft.azure.synapse.ml.cognitive.DetectMultivariateAnomaly"

    @staticmethod
    def _from_java(java_stage):
        module_name=DetectMultivariateAnomaly.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".DetectMultivariateAnomaly"
        return from_java(java_stage, module_name)

    def setBackoffs(self, value):
        """
        Args:
            backoffs: array of backoffs to use in the handler
        """
        self._set(backoffs=value)
        return self
    
    def setConcurrency(self, value):
        """
        Args:
            concurrency: max number of concurrent calls
        """
        self._set(concurrency=value)
        return self
    
    def setConcurrentTimeout(self, value):
        """
        Args:
            concurrentTimeout: max number seconds to wait on futures if concurrency >= 1
        """
        self._set(concurrentTimeout=value)
        return self
    
    def setConnectionString(self, value):
        """
        Args:
            connectionString: Connection String for your storage account used for uploading files.
        """
        self._set(connectionString=value)
        return self
    
    def setContainerName(self, value):
        """
        Args:
            containerName: Container that will be used to upload files to.
        """
        self._set(containerName=value)
        return self
    
    def setEndTime(self, value):
        """
        Args:
            endTime: A required field, end time of data to be used for detection/generating multivariate anomaly detection model, should be date-time.
        """
        self._set(endTime=value)
        return self
    
    def setEndpoint(self, value):
        """
        Args:
            endpoint: End Point for your storage account used for uploading files.
        """
        self._set(endpoint=value)
        return self
    
    def setErrorCol(self, value):
        """
        Args:
            errorCol: column to hold http errors
        """
        self._set(errorCol=value)
        return self
    
    def setInitialPollingDelay(self, value):
        """
        Args:
            initialPollingDelay: number of milliseconds to wait before first poll for result
        """
        self._set(initialPollingDelay=value)
        return self
    
    def setInputCols(self, value):
        """
        Args:
            inputCols: The names of the input columns
        """
        self._set(inputCols=value)
        return self
    
    def setIntermediateSaveDir(self, value):
        """
        Args:
            intermediateSaveDir: Directory name of which you want to save the intermediate data produced while training.
        """
        self._set(intermediateSaveDir=value)
        return self
    
    def setMaxPollingRetries(self, value):
        """
        Args:
            maxPollingRetries: number of times to poll
        """
        self._set(maxPollingRetries=value)
        return self
    
    def setModelId(self, value):
        """
        Args:
            modelId: Format - uuid. Model identifier.
        """
        self._set(modelId=value)
        return self
    
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
        self._set(outputCol=value)
        return self
    
    def setPollingDelay(self, value):
        """
        Args:
            pollingDelay: number of milliseconds to wait between polling
        """
        self._set(pollingDelay=value)
        return self
    
    def setSasToken(self, value):
        """
        Args:
            sasToken: SAS Token for your storage account used for uploading files.
        """
        self._set(sasToken=value)
        return self
    
    def setStartTime(self, value):
        """
        Args:
            startTime: A required field, start time of data to be used for detection/generating multivariate anomaly detection model, should be date-time.
        """
        self._set(startTime=value)
        return self
    
    def setStorageKey(self, value):
        """
        Args:
            storageKey: Storage Key for your storage account used for uploading files.
        """
        self._set(storageKey=value)
        return self
    
    def setStorageName(self, value):
        """
        Args:
            storageName: Storage Name for your storage account used for uploading files.
        """
        self._set(storageName=value)
        return self
    
    def setSubscriptionKey(self, value):
        """
        Args:
            subscriptionKey: the API key to use
        """
        if isinstance(value, list):
            value = SparkContext._active_spark_context._jvm.org.apache.spark.ml.param.ServiceParam.toSeq(value)
        self._java_obj = self._java_obj.setSubscriptionKey(value)
        return self
    
    def setSubscriptionKeyCol(self, value):
        """
        Args:
            subscriptionKey: the API key to use
        """
        self._java_obj = self._java_obj.setSubscriptionKeyCol(value)
        return self
    
    def setSuppressMaxRetriesExceededException(self, value):
        """
        Args:
            suppressMaxRetriesExceededException: set true to suppress the maxumimum retries exception and report in the error column
        """
        self._set(suppressMaxRetriesExceededException=value)
        return self
    
    def setTimeout(self, value):
        """
        Args:
            timeout: number of seconds to wait before closing the connection
        """
        self._set(timeout=value)
        return self
    
    def setTimestampCol(self, value):
        """
        Args:
            timestampCol: Timestamp column name
        """
        self._set(timestampCol=value)
        return self
    
    def setUrl(self, value):
        """
        Args:
            url: Url of the service
        """
        self._set(url=value)
        return self

    
    def getBackoffs(self):
        """
        Returns:
            backoffs: array of backoffs to use in the handler
        """
        return self.getOrDefault(self.backoffs)
    
    
    def getConcurrency(self):
        """
        Returns:
            concurrency: max number of concurrent calls
        """
        return self.getOrDefault(self.concurrency)
    
    
    def getConcurrentTimeout(self):
        """
        Returns:
            concurrentTimeout: max number seconds to wait on futures if concurrency >= 1
        """
        return self.getOrDefault(self.concurrentTimeout)
    
    
    def getConnectionString(self):
        """
        Returns:
            connectionString: Connection String for your storage account used for uploading files.
        """
        return self.getOrDefault(self.connectionString)
    
    
    def getContainerName(self):
        """
        Returns:
            containerName: Container that will be used to upload files to.
        """
        return self.getOrDefault(self.containerName)
    
    
    def getEndTime(self):
        """
        Returns:
            endTime: A required field, end time of data to be used for detection/generating multivariate anomaly detection model, should be date-time.
        """
        return self.getOrDefault(self.endTime)
    
    
    def getEndpoint(self):
        """
        Returns:
            endpoint: End Point for your storage account used for uploading files.
        """
        return self.getOrDefault(self.endpoint)
    
    
    def getErrorCol(self):
        """
        Returns:
            errorCol: column to hold http errors
        """
        return self.getOrDefault(self.errorCol)
    
    
    def getInitialPollingDelay(self):
        """
        Returns:
            initialPollingDelay: number of milliseconds to wait before first poll for result
        """
        return self.getOrDefault(self.initialPollingDelay)
    
    
    def getInputCols(self):
        """
        Returns:
            inputCols: The names of the input columns
        """
        return self.getOrDefault(self.inputCols)
    
    
    def getIntermediateSaveDir(self):
        """
        Returns:
            intermediateSaveDir: Directory name of which you want to save the intermediate data produced while training.
        """
        return self.getOrDefault(self.intermediateSaveDir)
    
    
    def getMaxPollingRetries(self):
        """
        Returns:
            maxPollingRetries: number of times to poll
        """
        return self.getOrDefault(self.maxPollingRetries)
    
    
    def getModelId(self):
        """
        Returns:
            modelId: Format - uuid. Model identifier.
        """
        return self.getOrDefault(self.modelId)
    
    
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
        return self.getOrDefault(self.outputCol)
    
    
    def getPollingDelay(self):
        """
        Returns:
            pollingDelay: number of milliseconds to wait between polling
        """
        return self.getOrDefault(self.pollingDelay)
    
    
    def getSasToken(self):
        """
        Returns:
            sasToken: SAS Token for your storage account used for uploading files.
        """
        return self.getOrDefault(self.sasToken)
    
    
    def getStartTime(self):
        """
        Returns:
            startTime: A required field, start time of data to be used for detection/generating multivariate anomaly detection model, should be date-time.
        """
        return self.getOrDefault(self.startTime)
    
    
    def getStorageKey(self):
        """
        Returns:
            storageKey: Storage Key for your storage account used for uploading files.
        """
        return self.getOrDefault(self.storageKey)
    
    
    def getStorageName(self):
        """
        Returns:
            storageName: Storage Name for your storage account used for uploading files.
        """
        return self.getOrDefault(self.storageName)
    
    
    def getSubscriptionKey(self):
        """
        Returns:
            subscriptionKey: the API key to use
        """
        return self.getOrDefault(self.subscriptionKey)
    
    
    def getSuppressMaxRetriesExceededException(self):
        """
        Returns:
            suppressMaxRetriesExceededException: set true to suppress the maxumimum retries exception and report in the error column
        """
        return self.getOrDefault(self.suppressMaxRetriesExceededException)
    
    
    def getTimeout(self):
        """
        Returns:
            timeout: number of seconds to wait before closing the connection
        """
        return self.getOrDefault(self.timeout)
    
    
    def getTimestampCol(self):
        """
        Returns:
            timestampCol: Timestamp column name
        """
        return self.getOrDefault(self.timestampCol)
    
    
    def getUrl(self):
        """
        Returns:
            url: Url of the service
        """
        return self.getOrDefault(self.url)

    

    
    def setLocation(self, value):
        self._java_obj = self._java_obj.setLocation(value)
        return self
    
    def cleanUpIntermediateData(self):
        self._java_obj.cleanUpIntermediateData()
        return
        